from .._tier0 import execute

def convolve (src, kernelImage, dst):
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
        "kernelImage":kernelImage,
        "dst":dst
    }

    execute(__file__, 'convolve_' + str(len(dst.shape)) + 'd_x.cl', 'convolve_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
