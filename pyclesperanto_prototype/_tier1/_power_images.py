from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def power_images(src1 : Image, src2 : Image, dst : Image = None):
    """Calculates x to the power of y pixel wise of two images X and Y.    Parameters
    ----------
    input : Image
    exponent : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.power_images(input, exponent, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_powerImages    

    """


    parameters = {
        "dst": dst,
        "src1":src1,
        "src2":src2
    }

    execute(__file__, 'power_images_' + str(len(dst.shape)) + 'd_x.cl', 'power_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
