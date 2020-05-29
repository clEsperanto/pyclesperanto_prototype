import inspect
from typing import Any, Callable, Dict, Optional, Sequence, Set, Type, Union
from functools import wraps
from toolz import curry

from gputools import OCLArray

from .create import create_like
from .types import Image, is_image
from .push import push

@curry
def plugin_function(
    function: Callable,
    output_creator: Callable = create_like
) -> Callable:
    """Function decorator which ensures correct types and values of parameters
        Given input parameters are either of type OCLArray (which the GPU understands) or are converted to this type
        (see push function). If output parameters of type OCLArray are not set, an empty image is created and handed
        over.

    :param function: the function to be called on the GPU
    :param output_creator: a function which can create an output OCLArray given an input OCLArray, optional
        per default, we create output images of the same shape as input images
    :return: return value of the executed function
    """


    @wraps(function)
    def worker_function(*args, **kwargs):
        # determine argument spec and default values, values are given as args
        argument_specification = inspect.getfullargspec(function)

        any_ocl_input = None

        for arg_counter, argument in enumerate(argument_specification.args):
            #print("---\nparsing argument " + argument)
            if (len(args) > arg_counter):
                value = args[arg_counter]
            else:
                value = None

            if (is_image(value)):
                value = push(value)
                # value is for sure OpenCL, we keep it in case we have to create another one of the same size
                any_ocl_input = value

            # default: keep value
            if (value is not None):
                kwargs[argument] = value


        # go through all arguments again and check if an image wasn't set
        for argument in argument_specification.args:
            if (kwargs.get(argument) is not None):
                value = kwargs[argument]
            else:
                value = None

            # was the argument annotated?
            type_annotation = argument_specification.annotations.get(argument);
            if (value is None):
                if (type_annotation is Image):
                    # if not set and should be an image, create an image
                    # create a new output image with specified/default creator
                    kwargs[argument] = output_creator(any_ocl_input)

        #print("Got arguments")
        #print(args)
        #print("Will pass arguments")
        #print(kwargs)

        # execute function with determined arguments
        return function(**kwargs)


    return worker_function
