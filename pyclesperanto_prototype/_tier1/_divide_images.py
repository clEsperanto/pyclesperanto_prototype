from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'in assistant'], priority=-1)
def divide_images(divident : Image, divisor : Image, destination : Image = None):
    """Divides two images X and Y by each other pixel wise. 
    
    <pre>f(x, y) = x / y</pre> 
    
    Parameters
    ----------
    divident : Image
    divisor : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.divide_images(divident, divisor, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_divideImages
    """


    parameters = {
        "src":divident,
        "src1":divisor,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/divide_images_' + str(len(destination.shape)) + 'd_x.cl', 'divide_images_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
