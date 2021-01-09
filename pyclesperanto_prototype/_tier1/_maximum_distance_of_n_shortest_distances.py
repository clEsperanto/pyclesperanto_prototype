from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_square_matrix

@plugin_function(output_creator=create_vector_from_square_matrix)
def maximum_distance_of_n_shortest_distances(distance_matrix : Image, distance_vector_destination: Image = None, n : int = 1):
    """Determines the n shortest distances for each column in a distance matrix and puts the maximum of these in a
    vector.

    Parameters
    ----------
    distance_matrix
    distance_vector_destination
    n

    Returns
    -------
    distance_vector_destination
    """

    parameters = {
        "src_distancematrix": distance_matrix,
        "dst_distancelist": distance_vector_destination,
        "nPoints" : int(n)
    }

    # todo: rename kernel function to fulfill naming conventions
    execute(__file__, 'maximum_distance_of_n_shortest_distances_x.cl',
            'maximum_distance_of_n_closest_points', distance_vector_destination.shape,
            parameters)

    return distance_vector_destination

