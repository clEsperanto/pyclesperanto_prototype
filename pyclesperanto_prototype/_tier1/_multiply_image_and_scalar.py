from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def multiply_image_and_scalar(src : Image, dst : Image = None, scalar : None = 0):
    """Multiplies all pixels value x in a given image X with a constant scalar s.
    
    <pre>f(x, s) = x * s</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number scalar)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_multiplyImageAndScalar


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst": dst,
        "scalar":float(scalar)
    }

    execute(__file__, 'multiply_image_and_scalar_' + str(len(dst.shape)) + 'd_x.cl', 'multiply_image_and_scalar_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
