from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import add_images_weighted

@plugin_function(categories=['combine', 'in assistant'], priority=-1)
def add_images(summand1 : Image, summand2 : Image, destination : Image = None):
    """Calculates the sum of pairs of pixels x and y of two images X and Y.
    
    <pre>f(x, y) = x + y</pre>
    
    Parameters
    ----------
    summand1 : Image
        The first input image to added.
    summand2 : Image
        The second image to be added.
    destination : Image
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_addImages
    """
    return add_images_weighted(summand1, summand2, destination, 1, 1)
