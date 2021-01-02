from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def add_image_and_scalar(source : Image, destination : Image = None, scalar : float = 1):
    """Adds a scalar value s to all pixels x of a given image X.
    
    <pre>f(x, s) = x + s</pre>
    
    Parameters
    ----------
    source : Image
        The input image where scalare should be added.
    destination : Image
        The output image where results are written into.
    scalar : float
        The constant number which will be added to all pixels.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.add_image_and_scalar(source, destination, scalar)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_addImageAndScalar
    """


    parameters = {
        "src":source,
        "dst":destination,
        "scalar":float(scalar)
    }
    execute(__file__, '../clij-opencl-kernels/kernels/add_image_and_scalar_' + str(len(destination.shape)) + 'd_x.cl', 'add_image_and_scalar_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination
