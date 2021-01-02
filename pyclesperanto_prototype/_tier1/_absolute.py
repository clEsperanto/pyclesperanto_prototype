from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def absolute(source : Image, destintation : Image = None):
    """Computes the absolute value of every individual pixel x in a given image.
    
    <pre>f(x) = |x| </pre>
    
    Parameters
    ----------
    source : Image
        The input image to be processed.
    destination : Image
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.absolute(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_absolute
    """


    parameters = {
        "src":source,
        "dst":destintation
    }

    execute(__file__, '../clij-opencl-kernels/kernels/absolute_' + str(len(destintation.shape)) + 'd_x.cl', 'absolute_' + str(len(destintation.shape)) + 'd', destintation.shape, parameters)
    return destintation
