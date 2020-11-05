from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def sobel(src : Image, dst : Image = None):
    """Convolve the image with the Sobel kernel.    Author(s): Ruth Whelan-Jeans, Robert Haase

    Parameters
    ----------
    source : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.sobel(, source, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sobel    

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'sobel_' + str(len(dst.shape)) + 'd_x.cl', 'sobel_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst