from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def laplace_diamond(src : Image, dst : Image = None):
    """Applies the Laplace operator (Diamond neighborhood) to an image.    Parameters
    ----------
    input : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.laplace_diamond(, input, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_laplaceDiamond    

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'laplace_diamond_' + str(len(dst.shape)) + 'd_x.cl', 'laplace_diamond_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
