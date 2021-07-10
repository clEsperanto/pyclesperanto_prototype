from .._tier0 import radius_to_kernel_size, execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'denoise', 'in assistant'])
def median_box(source : Image, destination : Image = None, radius_x : int = 1, radius_y : int = 1, radius_z : int = 1):
    """Computes the local median of a pixels box shaped neighborhood.

    The box is specified by its half-width and half-height (radius).
    For technical reasons, the area of the box must have less than 1000 pixels.
    
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
    >>> cle.median_box(source, destination, radius_x, radius_y, radius_z)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_median3DBox
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
    execute(__file__, '../clij-opencl-kernels/kernels/median_box_' + str(len(destination.shape)) + 'd_x.cl', 'median_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination