from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def power(src : Image, dst : Image = None, exponent : float = 1):
    """Computes all pixels value x to the power of a given exponent a.
    
    <pre>f(x, a) = x ^ a</pre>    Parameters
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
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_power    

    """


    parameters = {
        "src":src,
        "dst": dst,
        "exponent":float(exponent)
    }

    execute(__file__, 'power_' + str(len(dst.shape)) + 'd_x.cl', 'power_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
