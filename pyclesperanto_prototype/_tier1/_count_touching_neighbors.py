from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_square_matrix

@plugin_function(output_creator=create_vector_from_square_matrix)
def count_touching_neighbors(touch_matrix: Image, count_vector_destination: Image = None):
    """

    Parameters
    ----------
    touch_matrix
    count_vector_destination

    Returns
    -------

    """
    parameters = {
        "src_touch_matrix": touch_matrix,
        "dst_count_list": count_vector_destination
    }

    execute(__file__, 'count_touching_neighbors_x.cl',
            'count_touching_neighbors', count_vector_destination.shape,
            parameters)

    return count_vector_destination

