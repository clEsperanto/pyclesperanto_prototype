from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'edge detection', 'in assistant'])
def gradient_z(source : Image, destination : Image = None):
    """Computes the gradient of gray values along Z. 
    
    Assuming a, b and c are three adjacent
     pixels in Z direction. In the target image will be saved as: <pre>b' = 
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
    >>> cle.gradient_z(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientZ
    """


    parameters = {
        "dst":destination,
        "src":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/gradient_z_3d_x.cl', 'gradient_z_3d', destination.shape, parameters)
    return destination
