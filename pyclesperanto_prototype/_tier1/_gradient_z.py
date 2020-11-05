from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def gradient_z(src : Image, dst : Image = None):
    """Computes the gradient of gray values along Z. 
    
    Assuming a, b and c are three adjacent
     pixels in Z direction. In the target image will be saved as: <pre>b' = c - a;</pre>    Parameters
    ----------
    source : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.gradient_z(, source, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientZ    

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'gradient_z_3d_x.cl', 'gradient_z_3d', dst.shape, parameters)
    return dst
