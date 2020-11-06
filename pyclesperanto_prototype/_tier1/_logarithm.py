from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def logarithm(src : Image, dst : Image = None):
    """Computes base e logarithm of all pixels values.
    
    f(x) = log(x)     Author(s): Peter Haub, Robert Haase



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
    >>> cle.logarithm(source, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_logarithm    

    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'logarithm_' + str(len(dst.shape)) + 'd_x.cl', 'logarithm_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
