import inspect
from typing import Any, Callable, Dict, Optional, Sequence, Set, Type, Union
from functools import wraps
from toolz import curry

from ._pycl import OCLArray

from ._create import create_like
from ._types import Image, is_image
from ._push import push


@curry
def plugin_function(
    function: Callable,
    output_creator: Callable = create_like
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

    Returns
    -------
    worker_function : callable
        The actual function call that will be executed, magically creating
        output arguments of the correct type.
    """

    function.fullargspec = inspect.getfullargspec(function)

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


        # go through all arguments again and check if an image wasn't set,
        # in which case we create one.
        for argument in argument_specification.args:
            # was the argument annotated?
            type_annotation = argument_specification.annotations.get(argument);
            if argument not in kwargs:
                if type_annotation is Image:
                    # if not set and should be an image, create an image
                    # create a new output image with specified/default creator
                    kwargs[argument] = output_creator(*args)

        #print("Got arguments")
        #print(args)
        #print("Will pass arguments")
        #print(kwargs)

        # execute function with determined arguments
        return function(**kwargs)

    return worker_function
