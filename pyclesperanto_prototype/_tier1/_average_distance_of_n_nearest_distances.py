from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none

@plugin_function(output_creator=create_none)
def average_distance_of_n_nearest_distances(distance_matrix : Image, distance_vector_destination: Image = None, n : int = 1) -> Image:
    """Determines the n shortest distances for each column in a distance matrix and puts the average of these in a
    vector.

    Note: This function takes the distance to the identical label into account.

    Parameters
    ----------
    distance_matrix
    distance_vector_destination
    n

    Returns
    -------
    distance_vector_destination

    """
    from .._tier0 import create
    if distance_vector_destination is None:
        distance_vector_destination = create([1, distance_matrix.shape[1]])

    # todo: rename parameters in cl-kernel to make sense
    parameters = {
        "src_distancematrix": distance_matrix,
        "dst_indexlist": distance_vector_destination,
        "nPoints" : int(n)
    }

    # todo: rename kernel function to fulfill naming conventions
    execute(__file__, 'average_distance_of_n_nearest_distances_x.cl',
            'average_distance_of_n_nearest_distances', distance_vector_destination.shape,
            parameters)

    return distance_vector_destination

