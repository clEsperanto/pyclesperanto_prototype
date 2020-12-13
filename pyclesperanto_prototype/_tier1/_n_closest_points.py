from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import Image
from .._tier0 import execute

@plugin_function(output_creator=create_none)
def n_closest_points(distance_matrix : Image, indexlist_destination : Image = None, n : int = 1):
    """Determine the n point indices with shortest distance for all points in 
    a distance matrix. 
    
    This corresponds to the n row indices with minimum values for each column of 
    the distance matrix. 
    
    Parameters
    ----------
    distance_matrix : Image
    indexlist_destination : Image
    n : Number
    
    Returns
    -------
    indexlist_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_nClosestPoints
    """

    if indexlist_destination is None:
        indexlist_destination = create([int(n), distance_matrix.shape[1]])

    parameters = {
        "src_distancematrix":distance_matrix,
        "dst_indexlist":indexlist_destination,
    }

    # todo: rename cl-file kernel to fulfill naming conventions
    execute(__file__, "n_shortest_points_x.cl", "find_n_closest_points", distance_matrix.shape, parameters)

    return indexlist_destination
