from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def undefined_to_zero(source : Image, destination : Image = None):
    """Copies all pixels instead those which are not a number (NaN) or 
    infinity (inf), which are replaced by 0. 
    
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
    >>> cle.undefined_to_zero(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_undefinedToZero
    """


    parameters = {
        "dst":destination,
        "src":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/undefined_to_zero_x.cl', 'undefined_to_zero', destination.shape, parameters)
    return destination
