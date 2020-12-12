from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import Image
from .._tier0 import execute

@plugin_function(output_creator=create_none)
def n_closest_points(distance_matrix : Image, index_list : Image = None, n : int = 1):
    """

    Parameters
    ----------
    distance_matrix
    index_list
    n

    Returns
    -------

    """

    if index_list is None:
        index_list = create([int(n), distance_matrix.shape[1]])

    parameters = {
        "src_distancematrix":distance_matrix,
        "dst_indexlist":index_list,
    }

    # todo: rename cl-file kernel to fulfill naming conventions
    execute(__file__, "n_shortest_points_x.cl", "find_n_closest_points", distance_matrix.shape, parameters)

    return index_list
