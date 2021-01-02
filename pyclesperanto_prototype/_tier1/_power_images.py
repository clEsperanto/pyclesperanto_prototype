from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'in assistant'], priority=-1)
def power_images(input : Image, exponent : Image, destination : Image = None):
    """Calculates x to the power of y pixel wise of two images X and Y. 
    
    Parameters
    ----------
    input : Image
    exponent : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.power_images(input, exponent, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_powerImages
    """


    parameters = {
        "dst": destination,
        "src1":input,
        "src2":exponent
    }

    execute(__file__, '../clij-opencl-kernels/kernels/power_images_' + str(len(destination.shape)) + 'd_x.cl', 'power_images_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
