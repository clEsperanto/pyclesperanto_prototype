from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'in assistant'])
def maximum_images(source1 : Image, source2 : Image, destination : Image = None):
    """Computes the maximum of a pair of pixel values x, y from two given 
    images X and Y. 
    
    <pre>f(x, y) = max(x, y)</pre> 
    
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
    >>> cle.maximum_images(source1, source2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumImages
    """


    parameters = {
        "src":source1,
        "src1":source2,
        "dst": destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/maximum_images_' + str(len(destination.shape)) + 'd_x.cl', 'maximum_images_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
