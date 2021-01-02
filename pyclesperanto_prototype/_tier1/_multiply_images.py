from .._tier0 import execute

from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function(categories=['combine', 'in assistant'])
def multiply_images(factor1 : Image, factor2 : Image, destination : Image = None):
    """Multiplies all pairs of pixel values x and y from two image X and Y.
    
    <pre>f(x, y) = x * y</pre>
    
    Parameters
    ----------
    factor1 : Image
        The first input image to be multiplied.
    factor2 : Image
        The second image to be multiplied.
    destination : Image
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.multiply_images(factor1, factor2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyImages
    """


    parameters = {
        "src":factor1,
        "src1":factor2,
        "dst": destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/multiply_images_' + str(len(destination.shape)) + 'd_x.cl', 'multiply_images_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination