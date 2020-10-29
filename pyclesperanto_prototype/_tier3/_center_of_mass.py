from .._tier0 import Image
from .._tier0 import create_like
from .._tier1 import multiply_image_and_coordinate
from .._tier2 import sum_of_all_pixels

def center_of_mass(image : Image):
    """

    :return:
    """

    temp = create_like(image)

    sum = sum_of_all_pixels(image)

    multiply_image_and_coordinate(image, temp, 0)
    sum_x = sum_of_all_pixels(temp)

    multiply_image_and_coordinate(image, temp, 1)
    sum_y = sum_of_all_pixels(temp)

    multiply_image_and_coordinate(image, temp, 2)
    sum_z = sum_of_all_pixels(temp)

    return [sum_x / sum, sum_y / sum, sum_z / sum]

