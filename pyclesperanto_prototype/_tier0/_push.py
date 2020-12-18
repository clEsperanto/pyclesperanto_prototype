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
    import warnings
    warnings.warn(
            "Deprecated: The behaviour of `push()` will change in a future release. Switch to using push_zyx now to prevent issues in the future.",
            DeprecationWarning
        )

    if isinstance(any_array, OCLArray):
        return any_array

    transposed = any_array.astype(np.float32).T
    return OCLArray.from_array(transposed)


def push_zyx(any_array):
    if isinstance(any_array, OCLArray):
        return any_array

    temp = any_array.astype(np.float32)
    return OCLArray.from_array(temp)
