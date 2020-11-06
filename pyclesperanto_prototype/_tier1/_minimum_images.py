from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def minimum_images(src1 : Image, src2 : Image, dst : Image = None):
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
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumImages    

    """


    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'minimum_images_' + str(len(dst.shape)) + 'd_x.cl', 'minimum_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
