from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def maximum_sphere(source : Image, destination : Image = None, radius_x : float = 1, radius_y : float = 1, radius_z=0):
    """Computes the local maximum of a pixels spherical neighborhood. 
    
    The spheres size is specified by 
    its half-width, half-height and half-depth (radius). 
    
    Parameters
    ----------
    source : Image
    destination : Image
    radius_x : Number
    radius_y : Number
    radius_z : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.maximum_sphere(source, destination, radius_x, radius_y, radius_z)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximum3DSphere
    """


    kernel_size_x = radius_to_kernel_size(radius_x);
    kernel_size_y = radius_to_kernel_size(radius_y);
    kernel_size_z = radius_to_kernel_size(radius_z);

    parameters = {
        "dst":destination,
        "src":source,
        "Nx":int(kernel_size_x),
        "Ny":int(kernel_size_y)
    };

    if (len(destination.shape) == 3):
        parameters.update({"Nz":int(kernel_size_z)});
    execute(__file__, '../clij-opencl-kernels/kernels/maximum_sphere_' + str(len(destination.shape)) + 'd_x.cl', 'maximum_sphere_' + str(len(destination.shape)) + 'd', destination.shape, parameters);
    return destination