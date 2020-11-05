from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def maximum_images(src1 : Image, src2 : Image, dst : Image = None):
    """Computes the maximum of a pair of pixel values x, y from two given images X and Y. 
    
    <pre>f(x, y) = max(x, y)</pre>    Parameters
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
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumImages    

    """


    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'maximum_images_' + str(len(dst.shape)) + 'd_x.cl', 'maximum_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
