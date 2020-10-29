from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def power_images(src1 : Image, src2 : Image, dst : Image = None):
    """Calculates x to the power of y pixel wise of two images X and Y.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image input, Image exponent, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_powerImages


    Returns
    -------

    """


    parameters = {
        "dst": dst,
        "src1":src1,
        "src2":src2
    }

    execute(__file__, 'power_images_' + str(len(dst.shape)) + 'd_x.cl', 'power_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
