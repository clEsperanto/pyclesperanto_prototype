from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_ramp_x(source : Image):
    """Sets all pixel values to their X coordinate 
    
    Parameters
    ----------
    source : Image
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set_ramp_x(source)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setRampX
    """


    parameters = {
        "dst":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/set_ramp_x_' + str(len(source.shape)) + 'd_x.cl', 'set_ramp_x_' + str(len(source.shape)) + 'd', source.shape, parameters);
    return source
