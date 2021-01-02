from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_image_borders(destination : Image, value : float = 0):
    """Sets all pixel values at the image border to a given value. 
    
    Parameters
    ----------
    destination : Image
    value : Number
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set_image_borders(destination, value)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setImageBorders
    """


    parameters = {
        "dst":destination,
        "value":float(value)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/set_image_borders_' + str(len(destination.shape)) + 'd_x.cl', 'set_image_borders_' + str(len(destination.shape)) + 'd', destination.shape, parameters);
    return destination
