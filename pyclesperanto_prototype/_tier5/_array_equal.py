import numpy as np

from .._tier0 import plugin_function, Image
from .._tier0 import create_like, create_labels_like
from .._tier1 import erode_sphere, erode_box, multiply_images, copy
from .._tier4 import dilate_labels


@plugin_function(categories=['combine'])
def array_equal(source1: Image, source2: Image) -> bool:
    """Compares if all pixels of two images are identical. If shape of the images or any pixel
    are different, returns False. True otherwise

    This function is supposed to work similarly like its counterpart in numpy [1].

    Parameters
    ----------
    source1: Image
    source2: Image

    Returns
    -------
    bool

    References
    ----------
    ..[1] https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html
    """
    from .._tier4 import mean_squared_error
    if not np.array_equal(source1.shape, source2.shape):
        return False

    return mean_squared_error(source1, source2) == 0
