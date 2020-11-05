
from .._tier0 import execute
from .._tier0 import create_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def add_images_weighted(input1:Image, input2:Image, output :Image = None, weight1:float=1, weight2:float=1):
    """Calculates the sum of pairs of pixels x and y from images X and Y weighted with factors a and b.
    
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
        The constant number which will be multiplied with each pixel of summand1 before adding it.
    factor2 : float
        The constant number which will be multiplied with each pixel of summand2 before adding it.
        
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.add_images_weighted(summand1, summand2, destination, factor1, factor2)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_addImagesWeighted    

    """

    parameters = {
        "src":input1,
        "src1":input2,
        "dst":output,
        "factor":float(weight1),
        "factor1":float(weight2)
    }

    execute(__file__, 'add_images_weighted_' + str(len(output.shape)) + 'd_x.cl', 'add_images_weighted_' + str(len(output.shape)) + 'd', output.shape, parameters)

    return output
