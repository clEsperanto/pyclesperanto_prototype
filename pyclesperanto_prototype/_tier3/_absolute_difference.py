from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import create_like
from pyclesperanto_prototype._tier2 import subtract_images
from pyclesperanto_prototype._tier1 import absolute

@plugin_function(categories=['combine', 'in assistant'])
def absolute_difference(source1 : Image, source2 : Image, destination : Image = None):
    """Determines the absolute difference pixel by pixel between two images.
    
    <pre>f(x, y) = |x - y| </pre>
    
    Parameters
    ----------
    source1 : Image
        The input image to be subtracted from.
    source2 : Image
        The input image which is subtracted.
    destination : Image
        The output image  where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.absolute_difference(source1, source2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_absoluteDifference
    """

    temp = create_like(destination)

    subtract_images(source1, source2, temp)

    return absolute(temp, destination)