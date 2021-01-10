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

    index_list = n_closest_points(distance_matrix, n=n)

    set(touch_matrix_destination, 0)

    touch_matrix_destination = point_index_list_to_touch_matrix(index_list, touch_matrix_destination)

    return touch_matrix_destination