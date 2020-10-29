from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def absolute(src : Image, dst : Image = None):
    """Computes the absolute value of every individual pixel x in a given image.
    
    <pre>f(x) = |x| </pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_absolute


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'absolute_' + str(len(dst.shape)) + 'd_x.cl', 'absolute_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
