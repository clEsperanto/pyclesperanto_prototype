from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import execute
from .._tier0 import create_square_matrix_from_pointlist

@plugin_function(output_creator=create_square_matrix_from_pointlist)
def point_index_list_to_touch_matrix(indexlist : Image, matrix_destination : Image = None):
    """Takes a list of point indices to generate a touch matrix (a.k.a. adjacency graph matrix) out of it. The list has
    a dimensionality of m*n for the points 1... m (0 a.k.a. background is not in this list). In the n rows, there are
    indices to points which should be connected.
    
    Parameters
    ----------
    indexlist : Image
    matrix_destination : Image
    
    Returns
    -------
    matrix_destination
    """
    from .._tier1 import set
    set(matrix_destination, 0)

    parameters = {
        "src_indexlist": indexlist,
        "dst_matrix": matrix_destination,
    }

    dimensions = [1, 1, indexlist.shape[-1]]

    execute(__file__, "point_index_list_to_touch_matrix_x.cl", "point_index_list_to_touch_matrix", dimensions, parameters)

    return matrix_destination
