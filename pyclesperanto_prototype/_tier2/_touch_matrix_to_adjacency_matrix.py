from pyclesperanto_prototype._tier0 import create_square_matrix_from_labelmap
from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image

@plugin_function
def touch_matrix_to_adjacency_matrix(touch_matrix :Image, adjacency_matrix_destination :Image = None, self_adjacent : bool = True):
    from .._tier1 import set
    """Takes touch matrix (which is typically just half-filled) and makes a symmetrical adjacency matrix out of it.
    
    Furthermore, one can define if an object is adjacent to itself (default: True).
    
    Parameters
    ----------
    touch_matrix : Image
    adjacency_matrix_destination : Image
    self_adjacent : bool
        Default: true
        
    Returns
    -------
    adjacency_matrix_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_adjacencyMatrixToTouchMatrix
    """
    from .._tier1 import transpose_xy
    from .._tier1 import binary_or
    from .._tier1 import set_where_x_equals_y

    temp = transpose_xy(touch_matrix)
    adjacency_matrix_destination = binary_or(touch_matrix, temp, adjacency_matrix_destination)
    if self_adjacent:
        set_where_x_equals_y(adjacency_matrix_destination, 1)

    return adjacency_matrix_destination