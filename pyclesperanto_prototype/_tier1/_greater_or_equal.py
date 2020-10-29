from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def greater_or_equal(src1 : Image, src2 : Image, dst : Image = None):
    """Determines if two images A and B greater or equal pixel wise. 
    
    f(a, b) = 1 if a >= b; 0 otherwise. 

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source1, Image source2, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_greaterOrEqual


    Returns
    -------

    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'greater_or_equal_' + str(len(dst.shape)) + 'd_x.cl', 'greater_or_equal_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
