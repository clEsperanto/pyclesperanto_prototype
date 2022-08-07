import numpy as np

from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

@plugin_function
def sign(source : Image, destination : Image = None) -> Image:
    """Extracts the sign of pixels. If a pixel value < 0, resulting pixel value will be -1.
    If it was > 0, it will be 1. Otherwise it will be 0.

    This function aims to work similarly as its counterpart in numpy [1].

    Parameters
    ----------
    source : Image
    destination : Image, optional

    Returns
    -------
    destination
    
    See also
    --------
    ..[1] https://numpy.org/doc/stable/reference/generated/numpy.sign.html
    """

    parameters = {
        "dst":destination,
        "src":source
    }

    execute(__file__, 'sign.cl', 'sign', destination.shape, parameters)
    return destination
