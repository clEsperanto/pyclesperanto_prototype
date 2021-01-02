from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def draw_box(destination: Image, x: int = 0, y: int = 0, z: int = 0, width: int = 1, height: int = 1, depth: int = 1, value : float = 1):
    """Draws a box at a given start point with given size. 
    All pixels other than in the box are untouched. Consider using `set(buffer, 
    0);` in advance. 
    
    Parameters
    ----------
    destination : Image
    x : Number
    y : Number
    z : Number
    width : Number
    height : Number
    depth : Number
    value : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.draw_box(destination, x, y, z, width, height, depth, value)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_drawBox
    """


    if (len(destination.shape) == 2):
        parameters = {
            "dst": destination,
            "x1": float(x),
            "y1": float(y),
            "x2": float(x + width),
            "y2": float(y + height),
            "value": float(value)
        }
    else: # 3D
        parameters = {
            "dst": destination,
            "x1": float(x),
            "y1": float(y),
            "z1": float(z),
            "x2": float(x + width),
            "y2": float(y + height),
            "z2": float(z + depth),
            "value": float(value)
        }

    execute(__file__, '../clij-opencl-kernels/kernels/draw_box_' + str(len(destination.shape)) + 'd_x.cl', 'draw_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
