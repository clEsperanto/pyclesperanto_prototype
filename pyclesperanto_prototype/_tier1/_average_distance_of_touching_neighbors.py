from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_square_matrix

@plugin_function(output_creator=create_vector_from_square_matrix)
def average_distance_of_touching_neighbors(distance_matrix : Image, touch_matrix: Image, distance_vector_destination: Image = None):
    """

    Parameters
    ----------
    distance_matrix
    touch_matrix
    distance_vector_destination

    Returns
    -------

    """
    parameters = {
        "src_distance_matrix": distance_matrix,
        "src_touch_matrix": touch_matrix,
        "dst_average_distance_list": distance_vector_destination
    }

    execute(__file__, 'average_distance_of_touching_neighbors_x.cl',
            'average_distance_of_touching_neighbors', distance_vector_destination.shape,
            parameters)

    return distance_vector_destination

