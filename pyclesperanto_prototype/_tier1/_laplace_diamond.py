from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'edge detection'])
def laplace_diamond(source : Image, destination : Image = None):
    """Applies the Laplace operator (Diamond neighborhood) to an image. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.laplace_diamond(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_laplaceDiamond
    """


    parameters = {
        "dst":destination,
        "src":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/laplace_diamond_' + str(len(destination.shape)) + 'd_x.cl', 'laplace_diamond_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
