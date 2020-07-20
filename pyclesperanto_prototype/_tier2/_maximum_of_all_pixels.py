from .._tier0 import create
from .._tier0 import pull

def maximum_of_all_pixels(input):
    from .._tier1 import maximum_x_projection
    from .._tier1 import maximum_y_projection
    from .._tier1 import maximum_z_projection

    """

    :param input:
    :return:
    """

    dimensionality = input.shape

    if (len(dimensionality) == 3): # 3D image

        temp = create([dimensionality[1], dimensionality[2]])

        maximum_z_projection(input, temp)

        input = temp

        dimensionality = input.shape

    if (len(dimensionality) == 2): # 2D image (or projected 3D)

        temp = create([1, dimensionality[1]])

        maximum_y_projection(input, temp)

        input = temp

    temp = create([1, 1])

    maximum_x_projection(input, temp)

    return pull(temp)[0][0]

