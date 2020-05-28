import inspect
from typing import Any, Callable, Dict, Optional, Sequence, Set, Type, Union
from functools import wraps
from toolz import curry

from gputools import OCLArray

from .create import create_like
from .types import Image, isImage
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
        defaults_values = argument_specification.defaults

        target_arguments = {} # empty dictionary to store parameters as we forward them

        arg_counter = 0
        default_counter = 0
        any_ocl_input = None
        for argument in argument_specification.args:
            #print("---\nparsing argument " + argument)
            if (len(args) > arg_counter):
                value = args[arg_counter]
                #print("value")
                #print(value)
            else:
                value = None

            if (isImage(value)):
                value = push(value)
                # value is for sure OpenCL, we keep it in case we have to create another one of the same size
                any_ocl_input = value

            # default: keep value
            target_arguments.update({argument: value})

            # was the argument annotated?
            type_annotation = argument_specification.annotations.get(argument);
            if (value is None):
                if (type_annotation is Image):
                    # if not set and should be an image, create an image
                    print("E " + argument)
                    # create a new output image with specified/default creator
                    target_arguments.update({argument: output_creator(any_ocl_input)})
                else:
                    # if it's not set and should be something else than an image, hand over default values
                    if (len(defaults_values) > default_counter):
                        print("I " + argument)
                        target_arguments.update({argument: defaults_values[default_counter]})
                        default_counter += 1
                    else:
                        print("J " + argument + " to none")
                        target_arguments.update({argument: None})

            arg_counter += 1

        #print("Got arguments")
        #print(args)
        print("Will pass arguments")
        print(target_arguments)

        # execute function with determined arguments
        return function(**target_arguments)


    return worker_function










