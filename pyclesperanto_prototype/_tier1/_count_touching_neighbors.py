from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_square_matrix

@plugin_function(output_creator=create_vector_from_square_matrix)
def count_touching_neighbors(touch_matrix: Image, touching_neighbors_count_destination: Image = None, ignore_background:bool = True) -> Image:
    """Takes a touch matrix as input and delivers a vector with number of 
    touching neighbors per label as a vector.

    Note: Background is considered as something that can touch.
    To ignore touches with background, hand over a touch matrix where the
    first column (index = 0) has been set to 0. Use set_column for that.

    Parameters
    ----------
    touch_matrix : Image
    touching_neighbors_count_destination : Image, optional
    
    Returns
    -------
    touching_neighbors_count_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_countTouchingNeighbors
    """
    #parameters = {
    #    "src_touch_matrix": touch_matrix,
    #    "dst_count_list": touching_neighbors_count_destination
    #}
    #
    #execute(__file__, '../clij-opencl-kernels/kernels/count_touching_neighbors_x.cl',
    #        'count_touching_neighbors', touching_neighbors_count_destination.shape,
    #        parameters)
    from .._tier1 import sum_y_projection, set_row, set_column, set_where_x_equals_y
    #print("tm", touch_matrix)

    binary_matrix = touch_matrix > 0
    if ignore_background:
        set_row(binary_matrix, 0, 0)
        set_column(binary_matrix, 0, 0)
        set_where_x_equals_y(binary_matrix, 0)

    #print("bin_matrix", binary_matrix)

    touching_neighbors_count_destination = sum_y_projection(binary_matrix, touching_neighbors_count_destination)

    return touching_neighbors_count_destination

