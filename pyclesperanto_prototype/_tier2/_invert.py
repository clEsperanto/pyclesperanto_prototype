from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier1 import multiply_image_and_scalar

@plugin_function(categories=['filter'])
def invert(source : Image, destination :Image = None):
    """Computes the negative value of all pixels in a given image. 
    
    It is recommended to convert images to 
    32-bit float before applying this operation.
    
    <pre>f(x) = - x</pre>
    
    For binary images, use binaryNot. 
    
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
    >>> cle.invert(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_invert
    """

    multiply_image_and_scalar(source, destination, -1)

    return destination
