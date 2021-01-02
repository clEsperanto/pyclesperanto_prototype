from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_plane(source : Image, plane_index : int = 0, value : float = 0):
    """Sets all pixel values x of a given plane in X to a constant value v. 
    
    Parameters
    ----------
    source : Image
    plane_index : Number
    value : Number
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set_plane(source, plane_index, value)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setPlane
    """


    parameters = {
        "dst":source,
        "plane":int(plane_index),
        "value":float(value)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/set_plane_' + str(len(source.shape)) + 'd_x.cl', 'set_plane_' + str(len(source.shape)) + 'd', source.shape, parameters);
    return source
