from .._tier0 import execute
from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function
def mask(source : Image, mask : Image, destination : Image = None):
    """Computes a masked image by applying a binary mask to an image. 
    
    All pixel values x of image X will be copied
    to the destination image in case pixel value m at the same position in the 
    mask image is not equal to 
    zero.
    
    <pre>f(x,m) = (x if (m != 0); (0 otherwise))</pre> 
    
    Parameters
    ----------
    source : Image
    mask : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.mask(source, mask, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_mask
    """


    parameters = {
        "src":source,
        "mask":mask,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/mask_' + str(len(destination.shape)) + 'd_x.cl', 'mask_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination