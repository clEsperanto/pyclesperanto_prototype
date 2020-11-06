from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def multiply_image_and_scalar(src : Image, dst : Image = None, scalar : None = 0):
    """Multiplies all pixels value x in a given image X with a constant scalar s.
    
    <pre>f(x, s) = x * s</pre>
    
    Parameters
    ----------
    source : Image
        The input image to be multiplied with a constant.
    destination : Image
        The output image where results are written into.
    scalar : float
        The number with which every pixel will be multiplied with.
         
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.multiply_image_and_scalar(source, destination, scalar)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyImageAndScalar    

    """


    parameters = {
        "src":src,
        "dst": dst,
        "scalar":float(scalar)
    }

    execute(__file__, 'multiply_image_and_scalar_' + str(len(dst.shape)) + 'd_x.cl', 'multiply_image_and_scalar_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
