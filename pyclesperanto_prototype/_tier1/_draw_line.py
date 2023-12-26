from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['bia-bob-suggestion'])
def draw_line(destination : Image, x1 : float = 0, y1 : float = 0, z1 : float = 0, x2 : float = 1, y2 : float = 1, z2 : float = 1, thickness : float = 1, value : float = 1) -> Image:
    """Draws a line between two points with a given thickness. 
    
    All pixels other than on the line are untouched. Consider using 
    `set(buffer, 0);` in advance. 
    
    Parameters
    ----------
    destination : Image
    x1 : Number, optional
    y1 : Number, optional
    z1 : Number, optional
    x2 : Number, optional
    y2 : Number, optional
    z2 : Number, optional
    thickness : Number, optional
        technically specifying the radius including pixels around an inifitely thin line
    value : Number, optional
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.draw_line(destination, x1, y1, z1, x2, y2, z2, thickness, value)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_drawLine
    """


    if (len(destination.shape) == 2):
        parameters = {
            "dst": destination,
            "x1": float(x1),
            "y1": float(y1),
            "x2": float(x2),
            "y2": float(y2),
            "radius": float(thickness),
            "value": float(value)
        }
    else: # 3D
        parameters = {
            "dst": destination,
            "x1": float(x1),
            "y1": float(y1),
            "z1": float(z1),
            "x2": float(x2),
            "y2": float(y2),
            "z2": float(z2),
            "radius": float(thickness),
            "value": float(value)
        }

    # todo: rename cl file (missing _ between drawn and line)
    # todo: rname kernel name (upper case D should be lower case d)

    execute(__file__, '../clij-opencl-kernels/kernels/drawline_' + str(len(destination.shape)) + 'd_x.cl', 'draw_line_' + str(len(destination.shape)) + 'D', destination.shape, parameters)
    return destination
