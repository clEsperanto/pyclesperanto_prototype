from .._tier0 import create
from .._tier0 import pull

def sum_of_all_pixels(input):
    from .._tier1 import sum_x_projection
    from .._tier1 import sum_y_projection
    from .._tier1 import sum_z_projection

    """

    :param input:
    :return:
    """

    dimensionality = input.shape

    if (len(dimensionality) == 3): # 3D image

        temp = create([dimensionality[1], dimensionality[2]])

        sum_z_projection(input, temp)

        input = temp

        dimensionality = input.shape

    if (len(dimensionality) == 2): # 2D image (or projected 3D)

        temp = create([1, dimensionality[1]])

        sum_y_projection(input, temp)

        input = temp

    temp = create([1, 1])

    sum_x_projection(input, temp)

    return pull(temp)[0][0]

