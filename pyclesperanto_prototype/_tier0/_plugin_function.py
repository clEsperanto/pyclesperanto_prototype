import inspect
from typing import Any, Callable, Dict, Optional, Sequence, Set, Type, Union
from functools import wraps
from warnings import warn

from toolz import curry

from ._pycl import OCLArray

from ._create import create_like
from ._types import Image, is_image
from ._push import push


@curry
def plugin_function(
    function: Callable,
    output_creator: Callable = create_like,
    categories : list = None,
    priority : int = 0
) -> Callable:
    """Function decorator to ensure correct types and values of all parameters.

    The given input parameters are either of type OCLArray (which the GPU
    understands) or are converted to this type (see push function). If output
    parameters of type OCLArray are not set, an empty image is created and
    handed over.

    Parameters
    ----------
    function : callable
        The function to be executed on the GPU.
    output_creator : callable, optional
        A function to create an output OCLArray given an input OCLArray. By
        default, we create float32 output images of the same shape as input
        images.
    categories : list of str, optional
        A list of category names the function is associated with
    priority : int, optional
        can be used in lists of multiple operations to differentiate multiple operations that fulfill the same purpose
        but better/faster/more general.

    Returns
    -------
    worker_function : callable
        The actual function call that will be executed, magically creating
        output arguments of the correct type.
    """

    function.fullargspec = inspect.getfullargspec(function)
    function.categories = categories
    function.priority = priority

    @wraps(function)
    def worker_function(*args, **kwargs):
        # determine argument spec and default values, values are given as args
        argument_specification = inspect.getfullargspec(function)

        any_ocl_input = None

        for arg_counter, argument in enumerate(argument_specification.args):
            #print("---\nparsing argument " + argument)
            if arg_counter < len(args):
                value = args[arg_counter]
            else:
                value = None

            if is_image(value):
                value = push(value)
                # value is now for sure OpenCL, we keep it in case we have to
                # create another one of the same size
                any_ocl_input = value

            # default: keep value
            if value is not None:
                kwargs[argument] = value

        # accumulate args in a list in case only kwargs were passed
        args_list = []
        for argument in enumerate(argument_specification.args):
            try:
                value = kwargs[argument[1]]
                args_list = args_list + [value]
            except KeyError:
                break

        # go through all arguments again and check if an image wasn't set,
        # in which case we create one.
        for argument in argument_specification.args:
            # was the argument annotated?
            type_annotation = argument_specification.annotations.get(argument);
            if argument not in kwargs:
                if type_annotation is Image:
                    # if not set and should be an image, create an image
                    # create a new output image with specified/default creator
                    kwargs[argument] = output_creator(*args_list)

        # go through arguments again to check if one is passed that's not accepted on the other side
        # if for example a sigma array has been passed, but sigma_x, sigma_y and sigma_z are expected,
        # we convert the sigma array to three separate values
        keys_to_remove = []
        dict_to_append = {}
        for argument in kwargs.keys():
            if argument not in argument_specification.args:
                if argument + "_x" in argument_specification.args and \
                        argument + "_y" in argument_specification.args and \
                        argument + "_z" in argument_specification.args:

                    entry = kwargs[argument]
                    keys_to_remove.append(argument)

                    import numbers

                    if isinstance(entry, list):
                        if len(entry) == 3:
                            dict_to_append[argument + "_x"] = entry[2]
                            dict_to_append[argument + "_y"] = entry[1]
                            dict_to_append[argument + "_z"] = entry[0]
                        elif len(entry) == 2:
                            dict_to_append[argument + "_x"] = entry[1]
                            dict_to_append[argument + "_y"] = entry[0]
                        elif len(entry) == 1:
                            dict_to_append[argument + "_x"] = entry[0]
                            dict_to_append[argument + "_y"] = entry[0]
                            dict_to_append[argument + "_z"] = entry[0]
                    elif isinstance(entry, numbers.Number):
                        dict_to_append[argument + "_x"] = entry
                        dict_to_append[argument + "_y"] = entry
                        dict_to_append[argument + "_z"] = entry
                    else:
                        warn("Dropping parameter " + argument + " passed to " + function.__name__ + " because it the wrong type.")
                else:
                    warn(
                        "Dropping parameter " + argument + " passed to " + function.__name__ + " because it's not accepted.")

        for key in keys_to_remove:
            del kwargs[key]

        for key in dict_to_append.keys():
            kwargs[key] = dict_to_append[key]

        #print("Got arguments")
        #print(args)
        #print("Will pass arguments")
        #print(kwargs)

        # execute function with determined arguments
        return function(**kwargs)

    return worker_function
