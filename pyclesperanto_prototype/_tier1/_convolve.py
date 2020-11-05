from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def convolve(src : Image, kernel_image : Image, dst : Image = None):
    """Convolve the image with a given kernel image.
    
    It is recommended that the kernel image has an odd size in X, Y and Z.    Parameters
    ----------
    source : Image
    convolution_kernel : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.convolve(, source, , convolution_kernel, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_convolve    

    """


    parameters = {
        "src":src,
        "kernelImage":kernel_image,
        "dst":dst
    }

    execute(__file__, 'convolve_' + str(len(dst.shape)) + 'd_x.cl', 'convolve_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
