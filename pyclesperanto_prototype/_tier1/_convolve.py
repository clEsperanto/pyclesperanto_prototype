from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'combine', 'in assistant'])
def convolve(source : Image, convolution_kernel : Image, destination : Image = None):
    """Convolve the image with a given kernel image.
    
    It is recommended that the kernel image has an odd size in X, Y and Z. 
    
    Parameters
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
    >>> cle.convolve(source, convolution_kernel, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_convolve
    """


    parameters = {
        "src":source,
        "kernelImage":convolution_kernel,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/convolve_' + str(len(destination.shape)) + 'd_x.cl', 'convolve_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
