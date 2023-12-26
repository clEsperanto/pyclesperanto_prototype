from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'edge detection', 'in assistant', 'bia-bob-suggestion'])
def laplace_box(source : Image, destination : Image = None) -> Image:
    """Applies the Laplace operator (Box neighborhood) to an image. 
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    
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
        "src":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/laplace_box_' + str(len(destination.shape)) + 'd_x.cl', 'laplace_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
