from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'], priority=-1)
def power(source : Image, destination : Image = None, exponent : float = 1):
    """Computes all pixels value x to the power of a given exponent a.
    
    <pre>f(x, a) = x ^ a</pre> 
    
    Parameters
    ----------
    source : Image
    destination : Image
    exponent : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.power(source, destination, exponent)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_power
    """


    parameters = {
        "src":source,
        "dst": destination,
        "exponent":float(exponent)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/power_' + str(len(destination.shape)) + 'd_x.cl', 'power_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
