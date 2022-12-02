from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier1 import power

@plugin_function(categories=['filter'])
def square(source : Image, destination :Image = None) -> Image:
    """Return the element-wise square of the input.

    This function is supposed to be similar to its counterpart in numpy [1]
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://numpy.org/doc/stable/reference/generated/numpy.square.html
    """

    power(source, destination, 2)

    return destination
