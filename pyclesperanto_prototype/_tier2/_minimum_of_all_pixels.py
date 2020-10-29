from .._tier0 import create
from .._tier0 import pull
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def minimum_of_all_pixels(input : Image):
    from .._tier1 import minimum_x_projection
    from .._tier1 import minimum_y_projection
    from .._tier1 import minimum_z_projection

    """

    :param input:
    :return:
    """

    dimensionality = input.shape

    if (len(dimensionality) == 3): # 3D image

        temp = create([dimensionality[1], dimensionality[2]])

        minimum_z_projection(input, temp)

        input = temp

        dimensionality = input.shape

    if (len(dimensionality) == 2): # 2D image (or projected 3D)

        temp = create([1, dimensionality[1]])

        minimum_y_projection(input, temp)

        input = temp

    temp = create([1, 1])

    minimum_x_projection(input, temp)

    return pull(temp)[0][0]

