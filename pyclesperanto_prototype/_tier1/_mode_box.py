import warnings

from .._tier0 import radius_to_kernel_size, execute, create_none, create
from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_none)
def mode_box(source : Image, destination : Image = None, radius_x : int = 1, radius_y : int = 1, radius_z : int = 1) -> Image:
    """Computes the local mode of a pixels box shaped neighborhood.
    This can be used to post-process and locally correct semantic segmentation results.

    The box is specified by its half-width and half-height (radius).
    For technical reasons, the intensities must lie within a range from 0 to 255.
    In case multiple values have maximum frequency, the smallest one is returned.
    
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
    >>> cle.mode_box(source, destination, radius_x, radius_y, radius_z)
    
    """
    import numpy as np
    if source.dtype != np.uint8:
        warnings.warn("mode_box supports values between 0 and 255 only. Use pixel type uint8 for the source image to mute this warning.")

    if destination is None:
        destination = create(source, dtype=np.uint8)

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
    execute(__file__, 'mode_box_' + str(len(destination.shape)) + 'd_x.cl', 'mode_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination