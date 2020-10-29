from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def convolve(src : Image, kernel_image : Image, dst : Image = None):
    """Convolve the image with a given kernel image.
    
    It is recommended that the kernel image has an odd size in X, Y and Z.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, Image convolution_kernel, Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_convolve


    Returns
    -------

    """


    parameters = {
        "src":src,
        "kernelImage":kernel_image,
        "dst":dst
    }

    execute(__file__, 'convolve_' + str(len(dst.shape)) + 'd_x.cl', 'convolve_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
