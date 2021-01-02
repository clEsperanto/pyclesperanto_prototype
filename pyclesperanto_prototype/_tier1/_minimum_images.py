from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'in assistant'])
def minimum_images(source1 : Image, source2 : Image, destination : Image = None):
    """Computes the minimum of a pair of pixel values x, y from two given 
    images X and Y.
    
    <pre>f(x, y) = min(x, y)</pre> 
    
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
    >>> cle.minimum_images(source1, source2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumImages
    """


    parameters = {
        "src":source1,
        "src1":source2,
        "dst": destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/minimum_images_' + str(len(destination.shape)) + 'd_x.cl', 'minimum_images_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
