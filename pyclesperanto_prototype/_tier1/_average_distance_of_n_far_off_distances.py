from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_square_matrix

@plugin_function(output_creator=create_vector_from_square_matrix)
def average_distance_of_n_far_off_distances(distance_matrix : Image, distance_vector_destination: Image = None, n : int = 1):
    """Determines the n highest distances for each column in a distance matrix and puts the average of these in a
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

    # todo: rename parameters in cl-kernel to make sense
    parameters = {
        "src_distancematrix": distance_matrix,
        "dst_indexlist": distance_vector_destination,
        "nPoints" : int(n)
    }

    # todo: rename kernel function to fulfill naming conventions
    execute(__file__, '../clij-opencl-kernels/kernels/average_distance_of_n_far_off_distances_x.cl',
            'average_distance_of_n_far_off_points', distance_vector_destination.shape,
            parameters)

    return distance_vector_destination

