from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import multiply_matrix
from .._tier1 import greater_constant
from .._tier0 import create_like

@plugin_function
def neighbors_of_neighbors(touch_matrix : Image, neighbor_matrix_destination : Image = None, include_neighbors : bool = True):
    """Determines neighbors of neigbors from touch matrix and saves the result 
    as a new touch matrix. 
    
    Parameters
    ----------
    touch_matrix : Image
    neighbor_matrix_destination : Image
    include_neighbors : bool
        Defines wheather current neigbors should be include in the resulting neighborhood
    
    Returns
    -------
    neighbor_matrix_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_neighborsOfNeighbors
    """

    temp = create_like(touch_matrix)
    multiply_matrix(touch_matrix, touch_matrix, temp)

    if include_neighbors:
        from .._tier1 import binary_or
        neighbor_matrix_destination = binary_or(touch_matrix, temp, neighbor_matrix_destination)
    else:
        neighbor_matrix_destination = greater_constant(temp, neighbor_matrix_destination, 0)

    return neighbor_matrix_destination
