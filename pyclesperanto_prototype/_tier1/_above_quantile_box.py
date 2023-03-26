from .._tier0 import radius_to_kernel_size, execute
from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function(categories=['filter', 'edge detection', 'in assistant'])
def above_quantile_box(source : Image, destination : Image = None, radius_x : int = 1, radius_y : int = 1, radius_z : int = 1) -> Image:
    """Computes above which quantile (between 0 and 1) a pixel intensity lies with the pixels box shaped neighborhood.
    If the pixel is a local maximum, this filter will set it to value 1.
    If it's a local minimum, the value will become 0. The value is close to the local mean, the value will become 0.5.

    The box is specified by its half-width and half-height (radius).
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    radius_x : Number, optional
    radius_y : Number, optional
    radius_z : Number, optional
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.above_quantile_box(source, destination, radius_x, radius_y, radius_z)
    
    """
    kernel_size_x = radius_to_kernel_size(radius_x)
    kernel_size_y = radius_to_kernel_size(radius_y)
    kernel_size_z = radius_to_kernel_size(radius_z)

    parameters = {
        "dst":destination,
        "src":source,
        "Nx":int(kernel_size_x),
        "Ny":int(kernel_size_y)
    }

    if (len(destination.shape) == 3):
        parameters.update({"Nz":int(kernel_size_z)})
    execute(__file__, 'above_quantile_box_' + str(len(destination.shape)) + 'd_x.cl', 'above_quantile_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination