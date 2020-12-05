from .._tier1 import set
from .._tier0 import plugin_function
from .._tier0 import create
from .._tier0 import Image
from .._tier0 import execute
from .._tier1 import sum_x_projection
from .._tier1 import sum_y_projection

@plugin_function
def label_spots(binary_input : Image, labeling_destination : Image = None):
    """
    docs placeholder
    """

    set(labeling_destination, 0)

    dimensionality = binary_input.shape
    if (len(dimensionality) == 2):  # 2D image
        dimensionality = [1, dimensionality[0], dimensionality[1]]

    spot_count_per_x = create([dimensionality[1], dimensionality[2]])

    sum_x_projection(binary_input, spot_count_per_x)

    spot_count_per_xy = create([dimensionality[1], dimensionality[2]])

    sum_y_projection(spot_count_per_x, spot_count_per_xy)

    dims = [dimensionality[0], dimensionality[1], 1]

    parameters = {
        "dst": labeling_destination,
        "src": binary_input,
        "spotCountPerX": spot_count_per_x,
        "spotCountPerXY": spot_count_per_xy
    }

    execute(__file__, 'label_spots_in_x.cl', 'label_spots_in_x', dims, parameters)

    return labeling_destination