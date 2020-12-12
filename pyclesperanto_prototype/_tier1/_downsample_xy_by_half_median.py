from .._tier1 import copy
from .._tier0 import empty_image_like
from .._tier0 import push_zyx
from .._tier0 import push
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import create_image

@plugin_function(output_creator=create_none)
def downsample_xy_by_half_median(source : Image, destination : Image = None):
    """

    Parameters
    ----------
    source
    destination
    factor_x
    factor_y
    factor_z
    linear_interpolation

    Returns
    -------

    """

    factor_x = 0.5
    factor_y = 0.5
    factor_z = 1

    source_dimensions = source.shape
    if len(source_dimensions) == 2:
        destination_dimensions = [int(factor_y * source_dimensions[0]), int(factor_x * source_dimensions[1])]
    else:
        destination_dimensions = [int(factor_z * source_dimensions[0]), int(factor_y * source_dimensions[1]),
                                  int(factor_x * source_dimensions[2])]

    # create an output image in case none is given
    if destination is None:
        destination = create(destination_dimensions)

    parameters = {
        "dst": destination,
        "src": source,
    }

    execute(__file__, 'downsample_xy_by_half_median_3d' + '_x.cl',
            'downsample_xy_by_half_median_3d', destination.shape, parameters)

    return destination
