from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def reciprocal(source : Image, destination : Image = None) -> Image:
    """Computes 1/x for every pixel value

    This function is supposed to work similarly to its counter part in numpy [1]
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    
    Returns
    -------
    destination
    

    References
    ----------
    .. [1] https://numpy.org/doc/stable/reference/generated/numpy.reciprocal.html
    """
    parameters = {
        "src":source,
        "dst":destination
    }
    execute(__file__, 'reciprocal.cl', 'reciprocal', destination.shape, parameters)
    return destination
