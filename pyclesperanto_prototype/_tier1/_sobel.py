from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'edge detection', 'in assistant'])
def sobel(source : Image, destination : Image = None):
    """Convolve the image with the Sobel kernel. 
    
    Author(s): Ruth Whelan-Jeans, Robert Haase
    
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
    >>> cle.sobel(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sobel
    """


    parameters = {
        "dst":destination,
        "src":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/sobel_' + str(len(destination.shape)) + 'd_x.cl', 'sobel_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination