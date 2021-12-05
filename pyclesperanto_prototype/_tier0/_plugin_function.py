import inspect
from typing import Callable
from functools import wraps
from toolz import curry


from ._create import create_like
from ._types import Image, is_image
from ._push import push


@curry
def plugin_function(
    function: Callable,
    output_creator: Callable = create_like,
    categories: list = None,
    priority: int = 0,
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
        sig = inspect.signature(function)
        # create mapping from position and keyword arguments to parameters
        # will raise a TypeError if the provided arguments do not match the signature
        # https://docs.python.org/3/library/inspect.html#inspect.Signature.bind
        bound = sig.bind(*args, **kwargs)
        # set default values for missing arguments
        # https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults
        bound.apply_defaults()

        # copy images to GPU, and create output array if necessary
        for key, value in bound.arguments.items():
            if is_image(value):
                bound.arguments[key] = push(value)
            if key in sig.parameters and sig.parameters[key].annotation is Image and value is None:
                sig = inspect.signature(output_creator)
                bound.arguments[key] = output_creator(*bound.args[:len(sig.parameters)])

        # call the decorated function
        return function(*bound.args, **bound.kwargs)

    # this is necessary to obfuscate pyclesperanto's internal structure
    worker_function.__module__ = "pyclesperanto_prototype"

    return worker_function
