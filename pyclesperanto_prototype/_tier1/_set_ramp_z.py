from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_ramp_z(output : Image):
    """Sets all pixel values to their Z coordinate    Parameters
    ----------
    source : Image
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set_ramp_z(source)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setRampZ    

    """


    parameters = {
        "dst":output
    }

    execute(__file__, 'set_ramp_z_' + str(len(output.shape)) + 'd_x.cl', 'set_ramp_z_' + str(len(output.shape)) + 'd', output.shape, parameters);
    return output