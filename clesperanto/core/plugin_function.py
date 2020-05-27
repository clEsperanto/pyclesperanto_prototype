import inspect
from typing import Any, Callable, Dict, Optional, Sequence, Set, Type, Union
from functools import wraps
from toolz import curry

from gputools import OCLArray

from .create import create_like
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

        target_arguments = [None] * len(argument_specification.args)

        arg_counter = 0
        default_counter = 0
        any_input = None
        for argument in argument_specification.args:
            #print("---\nparsing argument " + argument)
            if (len(args) > arg_counter):
                value = args[arg_counter]
                #print("value")
                #print(value)
            else:
                value = None

            # was the argument annotated?
            type_annotation = argument_specification.annotations.get(argument);
            if (type_annotation is not None):
                if (type_annotation is OCLArray):
                    # annotated as OpenCL array
                    if (isinstance(value, OCLArray)):
                        # value is also OpenCL, pass it
                        target_arguments[arg_counter] = value
                        any_input = value
                    else:
                        # value is not OpenCL
                        if (value is not None):
                            # convert the value to OpenCL. push is magic and can convert anything
                            value = push(value)
                            any_input = value
                            target_arguments[arg_counter] = value
                        else:
                            # create a new output image with specified/default creator
                            target_arguments[arg_counter] = output_creator(any_input)

                else:
                    # any other type
                    target_arguments[arg_counter] = value
            else:
                # it wasn't annotated
                if (value is not None):
                    # if it's something, hand it over
                    target_arguments[arg_counter] = value
                else:
                    # if it's not set, hand over default values
                    if (len(defaults_values) > default_counter):
                        target_arguments[arg_counter] = defaults_values[default_counter]
                        default_counter += 1
                    else:
                        target_arguments[arg_counter] = None

            arg_counter += 1

        #print("Got arguments")
        #print(args)
        #print("Will pass arguments")
        #print(target_arguments)

        # execute function with determined arguments
        return function(*target_arguments)


    return worker_function










