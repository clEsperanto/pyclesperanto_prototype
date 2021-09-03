from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier3 import generate_proximal_neighbors_matrix
from .._tier1 import count_touching_neighbors
from .._tier1 import replace_intensities
import numpy as np

@plugin_function(categories=['label measurement', 'map', 'in assistant'], priority=1)
def proximal_neighbor_count_map(source : Image, destination : Image = None, min_distance : float = 0, max_distance : float = np.finfo(np.float32).max):
    """Takes a label map, determines which labels are within a give distance range
    and replaces every label with the number of neighboring labels.
    
     
    
    Parameters
    ----------
    source : Image
    destination : Image
    min_distance : float, optional
        default : 0
    max_distance : float, optional
        default: maximum float value
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_proximalNeighborCountMap
    """
    from .._tier1 import set_column
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix

    pointlist = centroids_of_labels(source)
    distance_matrix = generate_distance_matrix(pointlist, pointlist)

    touch_matrix = generate_proximal_neighbors_matrix(distance_matrix, min_distance=min_distance, max_distance=max_distance)
    number_of_touching_neighbors_vector = count_touching_neighbors(touch_matrix)

    # ignore how many objects touch the background
    set_column(number_of_touching_neighbors_vector, 0, 0)
    replace_intensities(source, number_of_touching_neighbors_vector, destination)
    return destination
