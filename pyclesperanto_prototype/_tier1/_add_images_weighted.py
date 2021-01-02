
from .._tier0 import execute
from .._tier0 import create_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'in assistant'])
def add_images_weighted(summand1:Image, summand2:Image, destination :Image = None, factor1:float=1, factor2:float=1):
    """Calculates the sum of pairs of pixels x and y from images X and Y 
    weighted with factors a and b.
    
    <pre>f(x, y, a, b) = x * a + y * b</pre>
    
    Parameters
    ----------
    summand1 : Image
        The first input image to added.
    summand2 : Image
        The second image to be added.
    destination : Image
        The output image where results are written into.
    factor1 : float
        The constant number which will be multiplied with each pixel of 
    summand1 before adding it.
    factor2 : float
        The constant number which will be multiplied with each pixel of 
    summand2 before adding it.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.add_images_weighted(summand1, summand2, destination, factor1, factor2)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_addImagesWeighted
    """

    parameters = {
        "src":summand1,
        "src1":summand2,
        "dst":destination,
        "factor":float(factor1),
        "factor1":float(factor2)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/add_images_weighted_' + str(len(destination.shape)) + 'd_x.cl', 'add_images_weighted_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination
