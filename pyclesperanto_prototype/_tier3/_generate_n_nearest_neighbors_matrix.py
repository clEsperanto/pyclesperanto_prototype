from .._tier0 import create_square_matrix_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def generate_n_nearest_neighbors_matrix(distance_matrix :Image, touch_matrix_destination :Image = None, n : int = 1):
    from .._tier1 import set
    """Produces a touch-matrix where the n nearest neighbors are marked as touching neighbors. 
    
    Takes a distance matrix (e.g. derived from a pointlist of centroids) and marks for every column the n smallest
    distances as neighbors. The resulting matrix can be use as if it was a touch-matrix (a.k.a. adjacency graph matrix). 
    
    Inspired by a similar implementation in imglib2 [1]
    
    Note: The implementation is limited to square matrices.
    
    Parameters
    ----------
    distance_marix : Image
    touch_matrix_destination : Image
    n : int
        number of neighbors
        
    References
    ----------
    [1] https://github.com/imglib/imglib2/blob/master/src/main/java/net/imglib2/interpolation/neighborsearch/InverseDistanceWeightingInterpolator.java
    
    Returns
    -------
    touch_matrix_destination
    """
    from .._tier1 import n_closest_points
    from .._tier1 import point_index_list_to_touch_matrix
    from .._tier1 import set
    from .._tier1 import set_row
    from .._tier1 import set_column
    from .._tier1 import set_where_x_equals_y
    from .._tier1 import copy
    import numpy as np

    distance_matrix = copy(distance_matrix)

    # ignore background and ignore self
    set_row(distance_matrix, 0, np.finfo(np.float32).max)
    set_column(distance_matrix, 0, np.finfo(np.float32).max)
    set_where_x_equals_y(distance_matrix, np.finfo(np.float32).max)

    index_list = n_closest_points(distance_matrix, n=n)

    set(touch_matrix_destination, 0)

    touch_matrix_destination = point_index_list_to_touch_matrix(index_list, touch_matrix_destination)

    set_column(touch_matrix_destination, 0, 0) # no label touches the background

    return touch_matrix_destination