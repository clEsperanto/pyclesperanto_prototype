from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def maximum_image_and_scalar(source : Image, destination : Image = None, scalar : float = 0):
    """Computes the maximum of a constant scalar s and each pixel value x in a 
    given image X. 
    
    <pre>f(x, s) = max(x, s)</pre> 
    
    Parameters
    ----------
    source : Image
    destination : Image
    scalar : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.maximum_image_and_scalar(source, destination, scalar)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumImageAndScalar
    """


    parameters = {
        "src":source,
        "dst": destination,
        "valueB":float(scalar)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/maximum_image_and_scalar_' + str(len(destination.shape)) + 'd_x.cl', 'maximum_image_and_scalar_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
