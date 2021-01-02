from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def subtract_image_from_scalar(input : Image, destination : Image = None, scalar : float = 0):
    """Subtracts one image X from a scalar s pixel wise.
    
    <pre>f(x, s) = s - x</pre> 
    
    Parameters
    ----------
    input : Image
    destination : Image
    scalar : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.subtract_image_from_scalar(input, destination, scalar)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_subtractImageFromScalar
    """


    parameters = {
        "src":input,
        "dst":destination,
        "scalar":float(scalar)
    }
    execute(__file__, '../clij-opencl-kernels/kernels/subtract_image_from_scalar_' + str(len(destination.shape)) + 'd_x.cl', 'subtract_image_from_scalar_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
