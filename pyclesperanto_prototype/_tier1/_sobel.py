from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def sobel(src : Image, dst : Image = None):
    """Convolve the image with the Sobel kernel.

    Author(s): Ruth Whelan-Jeans, Robert Haase

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_sobel


    Returns
    -------

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'sobel_' + str(len(dst.shape)) + 'd_x.cl', 'sobel_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst