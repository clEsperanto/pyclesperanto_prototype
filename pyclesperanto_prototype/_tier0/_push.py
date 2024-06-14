import warnings

import numpy as np
from ._backends import Backend

def push(any_array):
    """Copies an image to GPU memory and returns its handle

    .. deprecated:: 0.6.0
        `push` behaviour will be changed pyclesperanto_prototype 0.7.0 to do the same as
        `push_zyx` because it's faster and having both doing different things is confusing.
    
    Parameters
    ----------
    image : numpy array

    Returns
    -------
    object of type backend.array_type()
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.push(image)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_push
    """
    if hasattr(any_array, "is_cuda") and any_array.is_cuda:
        # special treatment for pytorch tensors
        any_array = any_array.cpu()

    if isinstance(any_array, Backend.get_instance().get().array_type()):
        return any_array

    if isinstance(any_array, list) or isinstance(any_array, tuple):
        any_array = np.asarray(any_array)

    if hasattr(any_array, 'shape') and hasattr(any_array, 'dtype') and hasattr(any_array, 'get'):
        any_array = np.asarray(any_array.get())

    not_supported_types = {
        np.float64: np.float32,
        np.int64: np.int32,
        np.uint64: np.int64
    }
    if any_array.dtype in not_supported_types.keys():
        replacement_type = not_supported_types[any_array.dtype]
        warnings.warn(f"dtype {any_array.dtype} not supported, converting to {replacement_type} instead")
        any_array = any_array.astype(replacement_type)

    return Backend.get_instance().get().from_array(any_array)


def push_zyx(any_array):
    
    warnings.warn(
        "Deprecated: `push_zyx()` is now deprecated as it does the same as `push()`.",
        DeprecationWarning
    )
    return push(any_array)

