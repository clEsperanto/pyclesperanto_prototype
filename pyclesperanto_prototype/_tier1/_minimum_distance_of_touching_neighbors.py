from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_square_matrix

@plugin_function(output_creator=create_vector_from_square_matrix)
def minimum_distance_of_touching_neighbors(distance_matrix : Image, touch_matrix: Image, distancelist_destination: Image = None):
    """Takes a touch matrix and a distance matrix to determine the minimum
    distance of touching neighbors for every object.
    
    Parameters
    ----------
    distance_matrix : Image
    touch_matrix : Image
    distancelist_destination : Image
    
    Returns
    -------
    average_distancelist_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumDistanceOfTouchingNeighbors
    """
    parameters = {
        "src_distance_matrix": distance_matrix,
        "src_touch_matrix": touch_matrix,
        "dst_distance_list": distancelist_destination
    }

    execute(__file__, 'minimum_distance_of_touching_neighbors_x.cl',
            'minimum_distance_of_touching_neighbors', distancelist_destination.shape,
            parameters)

    return distancelist_destination

