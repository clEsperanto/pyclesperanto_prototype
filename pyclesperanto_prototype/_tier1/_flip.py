from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def flip(source : Image, destination : Image = None, flip_x : bool = True, flip_y : bool = True, flip_z : bool = True):
    """Flips an image in X, Y and/or Z direction depending on boolean flags. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    flip_x : Boolean
    flip_y : Boolean
    flip_z : Boolean
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.flip(source, destination, flip_x, flip_y, flip_z)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_flip3D
    """


    parameters = {
        "src":source,
        "dst":destination,
        "flipx": int(1 if flip_x else 0),
        "flipy": int(1 if flip_y else 0)
    }

    if (len(destination.shape) == 3):
        parameters.update({"flipz": int(1 if flip_z else 0)});

    execute(__file__, '../clij-opencl-kernels/kernels/flip_' + str(len(destination.shape)) + 'd_x.cl', 'flip_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
