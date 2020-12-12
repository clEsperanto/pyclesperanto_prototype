from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import multiply_matrix
from .._tier1 import greater_constant
from .._tier0 import create_like

@plugin_function
def neighbors_of_neighbors(touch_matrix : Image, neighbor_neighbor_matrix : Image = None):
    """

    Parameters
    ----------
    touch_matrix
    neighbor_neighbor_matrix

    Returns
    -------

    """

    temp = create_like(touch_matrix)
    multiply_matrix(touch_matrix, touch_matrix, temp)
    neighbor_neighbor_matrix = greater_constant(temp, neighbor_neighbor_matrix, 0)
    return neighbor_neighbor_matrix
