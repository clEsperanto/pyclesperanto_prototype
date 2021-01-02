from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'edge detection', 'in assistant'])
def laplace_box(input : Image, destination : Image = None):
    """Applies the Laplace operator (Box neighborhood) to an image. 
    
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
    >>> cle.laplace_box(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_laplaceBox
    """


    parameters = {
        "dst":destination,
        "src":input
    }

    execute(__file__, '../clij-opencl-kernels/kernels/laplace_box_' + str(len(destination.shape)) + 'd_x.cl', 'laplace_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
