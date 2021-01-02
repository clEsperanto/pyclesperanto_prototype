from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'edge detection', 'in assistant'])
def gradient_x(source : Image, destination : Image = None):
    """Computes the gradient of gray values along X. 
    
    Assuming a, b and c are three adjacent
     pixels in X direction. In the target image will be saved as: <pre>b' = 
    c - a;</pre> 
    
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
    >>> cle.gradient_x(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientX
    """


    parameters = {
        "dst":destination,
        "src":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/gradient_x_' + str(len(destination.shape)) + 'd_x.cl', 'gradient_x_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
