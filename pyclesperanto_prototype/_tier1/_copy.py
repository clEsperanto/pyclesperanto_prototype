from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def copy(src : Image, dst : Image = None):
    """Copies an image.
    
    <pre>f(x) = x</pre>    Parameters
    ----------
    source : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.copy(, source, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_copy    

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'copy_' + str(len(dst.shape)) + 'd_x.cl', 'copy_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
