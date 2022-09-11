from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def generate_n_most_touching_neighbors_matrix(touch_amount_matrix: Image, touch_matrix_destination: Image = None,
                                              n: int = 1) -> Image:
    """Generates a touch matrix from a matrix describing how much labels touch
    by selecting the n neighbors most touching.

    touch_amount_matrix: Image
        can be either a touch-portion or touch-count
    touch_matrix_destination: Image, optional
    n: int, optional
        default: 1
    """
    from .._tier1 import reciprocal, set_where_x_equals_y, nan_to_num, set_row, set_column, greater_constant, binary_and
    from .._tier2 import maximum_of_all_pixels
    from .._tier3 import generate_n_nearest_neighbors_matrix

    temp1 = reciprocal(touch_amount_matrix)

    # ignore self-touching ; should be 0 anyway;
    # induces division by zero in the next step
    set_where_x_equals_y(temp1, 0)

    # eliminate self-touching and background-touching
    temp2 = nan_to_num(temp1)
    max_val = maximum_of_all_pixels(temp2)
    set_column(temp2, 0, max_val + 1)
    set_row(temp2, 0, max_val + 1)
    set_where_x_equals_y(temp2, max_val + 1)
    # print("n most touching:\n", temp2)

    # Figure out which labels actually touch
    temp3 = greater_constant(touch_amount_matrix, constant=0)
    set_column(temp3, 0, 0)
    set_row(temp3, 0, 0)
    set_where_x_equals_y(temp3, 0)
    # print("greater 0:\n", temp3)

    generate_n_nearest_neighbors_matrix(temp1, temp2, n=n)

    # mask with touch matrix
    binary_and(temp2, temp3, touch_matrix_destination)
    # print("binary and:\n", touch_matrix_destination)

    return touch_matrix_destination
