from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def minimum_sphere(input : Image, output : Image = None, radius_x : float = 1, radius_y : float = 1, radius_z : float = 1):
    """Computes the local minimum of a pixels spherical neighborhood. 
    
    The spheres size is specified by 
    its half-width, half-height and half-depth (radius). 

    Parameters
    ----------
    source : Image
    destination : Image
    radiusX : Number
    radiusY : Number
    radiusZ : Number
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.minimum_sphere(source, destination, radiusX, radiusY, radiusZ)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimum3DSphere    

    """


    kernel_size_x = radius_to_kernel_size(radius_x);
    kernel_size_y = radius_to_kernel_size(radius_y);
    kernel_size_z = radius_to_kernel_size(radius_z);

    parameters = {
        "dst":output,
        "src":input,
        "Nx":int(kernel_size_x),
        "Ny":int(kernel_size_y)
    };

    if (len(output.shape) == 3):
        parameters.update({"Nz":int(kernel_size_z)});
    execute(__file__, 'minimum_sphere_' + str(len(output.shape)) + 'd_x.cl', 'minimum_sphere_' + str(len(output.shape)) + 'd', output.shape, parameters);
    return output
