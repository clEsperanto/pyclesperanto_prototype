from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import radius_to_kernel_size


@plugin_function(categories=['filter', 'edge detection', 'in assistant'])
def variance_box(source: Image, destination: Image = None, radius_x : int = 1, radius_y : int = 1, radius_z : int = 1):
    """Computes the local variance of a pixels box neighborhood. \n\nThe box size is specified by
    its half-width, half-height and half-depth (radius). If 2D images are given, radius_z will be ignored.

    Parameters
    ----------
    source : Image
    destination : Image
    radius_x : int
    radius_y : int
    radius_z : int

    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.variance_box(source, destination, 10, 10, 10)

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_varianceBox
    """

    parameters = {
        "dst": destination,
        "src": source,
        "Nx": radius_to_kernel_size(radius_x),
        "Ny": radius_to_kernel_size(radius_y),
    }
    if (len(destination.shape) == 3):
        parameters.update({"Nz":radius_to_kernel_size(radius_z)})

    execute(__file__, 'variance_box_' + str(len(destination.shape)) + 'd_x.cl',
            'variance_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination

