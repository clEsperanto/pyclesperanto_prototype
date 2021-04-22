import numpy as np
from ._pycl import OCLArray


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
    OCLArray
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.push(image)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_push
    """
    if isinstance(any_array, OCLArray):
        return any_array

    if isinstance(any_array, list) or isinstance(any_array, tuple):
        any_array = np.asarray(any_array)

    float_arr = any_array.astype(np.float32)
    return OCLArray.from_array(float_arr)


def push_zyx(any_array):
    import warnings
    warnings.warn(
        "Deprecated: `push_zyx()` is now deprecated as it does the same as `push()`.",
        DeprecationWarning
    )
    return push(any_array)