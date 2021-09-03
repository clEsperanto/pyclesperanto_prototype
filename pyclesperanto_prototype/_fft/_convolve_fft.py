from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'combine', 'in assistant'])
def convolve_fft(source : Image, convolution_kernel : Image, destination: Image = None):
    """
    Convolve an image with a given kernel. The operation is executed in Fourier space

    Parameters
    ----------
    source : Image
        Image to be convolved
    convolution_kernel : Image
        Convolution kernel
    destination: Image, optional
        Result image

    Returns
    -------
    destination

    See Also
    --------
    .. [1] https://clij.github.io/clij2-docs/reference_convolve
    """
    from ._fftconvolve import fftconvolve
    from .._tier1 import copy
    result = fftconvolve(source, convolution_kernel)
    copy(result, destination)
    return destination