import numpy as np
from ._pycl import OCLArray


def push(any_array):
    """Copies an image specified by its name to GPU memory in order to process it there later.    Parameters
    ----------
    image : String
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.push(image)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_push    

    """

    if isinstance(any_array, OCLArray):
        return any_array

    transposed = any_array.astype(np.float32).T
    return OCLArray.from_array(transposed)


def push_zyx(any_array):
    if isinstance(any_array, OCLArray):
        return any_array

    temp = any_array.astype(np.float32)
    return OCLArray.from_array(temp)
