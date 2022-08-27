from .._tier0 import plugin_function
from .._tier1 import replace_intensities
from .._tier0 import Image
from .._tier0 import create_vector_from_labelmap

@plugin_function(categories=['label measurement'], output_creator=create_vector_from_labelmap)
def standard_deviation_touch_portion(labels : Image, std_touch_portion_vector_destination : Image = None) -> Image:
    """Measure touch portion of all labels to each other and determine the standard deviation of the touch portion for
    each label and write it into a vector.

    Parameters
    ----------
    labels: Image
    std_touch_portion_vector_destination: Image, optional

    Returns
    -------
    std_touch_portion_map_destination
    """
    from .._tier1 import generate_touch_matrix, set_row, set_column, set_where_x_equals_y, divide_images, nan_to_num
    from .._tier1 import sum_y_projection, reciprocal, multiply_images, absolute
    from .._tier2 import touch_matrix_to_adjacency_matrix
    from .._tier4 import generate_touch_portion_matrix

    touch_portion_matrix = generate_touch_portion_matrix(labels)

    # determine which objects touch
    touch_matrix = touch_matrix_to_adjacency_matrix(generate_touch_matrix(labels))
    set_where_x_equals_y(touch_matrix, 0)

    # count how many neigbors every label has, including background
    touch_count_vector = sum_y_projection(touch_matrix)

    # the average touch portion is per definition 1 / neighbor_count
    average_touch_portion = reciprocal(touch_count_vector)

    # we turn this vector into a matrix where only touching objects are set
    mean_portion_matrix = multiply_images(touch_matrix, average_touch_portion)

    # subtracting the mean touch portion from the touch portion gives us the deviation from the average
    absolute_deviation_matrix = absolute(touch_portion_matrix - mean_portion_matrix)

    # dividing it by count and summing over all labels gives us the standard deviation
    standard_deviation_matrix = divide_images(absolute_deviation_matrix, touch_count_vector)
    return nan_to_num(sum_y_projection(standard_deviation_matrix), std_touch_portion_vector_destination)
