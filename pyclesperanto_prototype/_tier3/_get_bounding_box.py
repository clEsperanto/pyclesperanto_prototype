from .._tier0._types import Image
from .._tier0 import create_like
from .._tier1 import multiply_image_and_coordinate
from .._tier2 import maximum_of_all_pixels
from .._tier2 import minimum_of_masked_pixels

def get_bounding_box(binary_image : Image):
    """
      :param input:
      :return:
    """

    temp = create_like(binary_image)

    multiply_image_and_coordinate(binary_image, temp, 0)
    max_x = maximum_of_all_pixels(temp)
    min_x = minimum_of_masked_pixels(temp, binary_image)
    print("min_x" + str(min_x))

    multiply_image_and_coordinate(binary_image, temp, 1)
    max_y = maximum_of_all_pixels(temp)
    min_y = minimum_of_masked_pixels(temp, binary_image)

    if len(binary_image.shape) == 3:
        multiply_image_and_coordinate(binary_image, temp, 2)
        max_z = maximum_of_all_pixels(temp)
        min_z = minimum_of_masked_pixels(temp, binary_image)

        return [min_x, min_y, min_z, max_x, max_y, max_z]
    else:
        return [min_x, min_y, 0, max_x, max_y, 0]
