from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def gradient_y(src : Image, dst : Image = None):
    """Computes the gradient of gray values along Y. 
    
    Assuming a, b and c are three adjacent
     pixels in Y direction. In the target image will be saved as: <pre>b' = c - a;</pre>    Parameters
    ----------
    source : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.gradient_y(, source, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientY    

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'gradient_y_' + str(len(dst.shape)) + 'd_x.cl', 'gradient_y_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
