from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_square_matrix

@plugin_function(output_creator=create_vector_from_square_matrix)
def count_touching_neighbors(touch_matrix: Image, touching_neighbors_count_destination: Image = None):
    """Takes a touch matrix as input and delivers a vector with number of 
    touching neighbors per label as a vector.

    Note: Background is considered as something that can touch.
    To ignore touches with background, hand over a touch matrix where the
    first column (index = 0) has been set to 0. Use set_column for that.

    Parameters
    ----------
    touch_matrix : Image
    touching_neighbors_count_destination : Image
    
    Returns
    -------
    touching_neighbors_count_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_countTouchingNeighbors
    """
    parameters = {
        "src_touch_matrix": touch_matrix,
        "dst_count_list": touching_neighbors_count_destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/count_touching_neighbors_x.cl',
            'count_touching_neighbors', touching_neighbors_count_destination.shape,
            parameters)

    return touching_neighbors_count_destination

