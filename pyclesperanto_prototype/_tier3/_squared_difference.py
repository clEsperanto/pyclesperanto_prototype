from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import create_like
from pyclesperanto_prototype._tier2 import subtract_images
from pyclesperanto_prototype._tier1 import power

@plugin_function(categories=['combine', 'in assistant'])
def squared_difference(source1 : Image, source2 : Image, destination : Image = None):
    """Determines the squared difference pixel by pixel between two images. 
    
    Parameters
    ----------
    source1 : Image
    source2 : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.squared_difference(source1, source2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_squaredDifference
    """

    temp = create_like(destination)

    subtract_images(source1, source2, temp)

    return power(temp, destination, 2)