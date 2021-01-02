from .._tier0 import execute


from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def draw_sphere(destination : Image, x : float = 0, y : float = 0, z : float = 0, radius_x : float = 1, radius_y : float = 1, radius_z : float = 1, value : float = 1):
    """Draws a sphere around a given point with given radii in x, y and z (if 
    3D). 
    
     All pixels other than in the sphere are untouched. Consider using 
    `set(buffer, 0);` in advance. 
    
    Parameters
    ----------
    destination : Image
    x : Number
    y : Number
    z : Number
    radius_x : Number
    radius_y : Number
    radius_z : Number
    value : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.draw_sphere(destination, x, y, z, radius_x, radius_y, radius_z, value)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_drawSphere
    """


    if (len(destination.shape) == 2):
        parameters = {
            "dst": destination,
            "cx": float(x),
            "cy": float(y),
            "rx": float(radius_x),
            "ry": float(radius_y),
            "rxsq": float(radius_x * radius_x),
            "rysq": float(radius_y * radius_y),
            "value": float(value)
        }
    else: # 3D
        parameters = {
            "dst": destination,
            "cx": float(x),
            "cy": float(y),
            "cz": float(z),
            "rx": float(radius_x),
            "ry": float(radius_y),
            "rz": float(radius_z),
            "rxsq": float(radius_x * radius_x),
            "rysq": float(radius_y * radius_y),
            "rzsq": float(radius_z * radius_z),
            "value": float(value)
        }

    execute(__file__, '../clij-opencl-kernels/kernels/draw_sphere_' + str(len(destination.shape)) + 'd_x.cl', 'draw_sphere_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
