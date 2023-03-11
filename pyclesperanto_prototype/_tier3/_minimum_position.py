from .._tier0 import create
from .._tier0 import pull
from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function
def minimum_position(source: Image) -> tuple:
    """Determines the position of the minimum of all pixels in a given image.

    Parameters
    ----------
    source : Image
        The image of which the position of the minimum of all pixels or voxels will be determined.

    Returns
    -------
    tuple

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.minimum_position(source)
    """
    from .._tier1 import minimum_x_projection
    from .._tier1 import minimum_y_projection
    from .._tier1 import minimum_z_projection
    from .._tier2 import x_position_of_minimum_x_projection
    from .._tier2 import y_position_of_minimum_y_projection
    from .._tier2 import z_position_of_minimum_z_projection

    # Find minimum projections and positions along each axis, reducing the dimensionality of the array
    # To have the same properties as ndi.minimum_position, find projections in the order X -> Y -> Z

    dimensionality = source.shape

    z_coord, y_coord, x_coord = 0, 0, 0
    pos_z, pos_y, pos_x = None, None, None
    min_position = []

    temp_min = minimum_x_projection(source)
    pos_x = x_position_of_minimum_x_projection(source)
    source = temp_min

    if len(dimensionality) > 1:
        temp_min = minimum_y_projection(source)
        pos_y = y_position_of_minimum_y_projection(source)
        source = temp_min

    if len(dimensionality) > 2:
        # Use x position as the updated input array is 2d
        pos_z = x_position_of_minimum_x_projection(source)

    # Use calculated max positions to find coordinates of each axis
    if pos_z is not None:
        z_coord = int(pos_z[0][0])
        min_position += [z_coord]

    if pos_y is not None:
        y_coord = int(pos_y[0][z_coord])
        min_position += [y_coord]

    if pos_x is not None:
        x_coord = int(pos_x[y_coord][z_coord])
        min_position += [x_coord]

    return tuple(min_position)
