from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def gradient_x(src : Image, dst : Image = None):
    """Computes the gradient of gray values along X. 
    
    Assuming a, b and c are three adjacent
     pixels in X direction. In the target image will be saved as: <pre>b' = c - a;</pre>    Parameters
    ----------
    source : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.gradient_x(source, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientX    

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'gradient_x_' + str(len(dst.shape)) + 'd_x.cl', 'gradient_x_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
