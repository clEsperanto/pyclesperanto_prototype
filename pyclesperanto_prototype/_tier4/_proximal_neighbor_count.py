from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np
from .._tier0 import create_none

@plugin_function(categories=['label measurement'], output_creator=create_none)
def proximal_neighbor_count(source : Image, destination : Image = None, min_distance : float = 0, max_distance : float = np.finfo(np.float32).max) -> Image:
    """Takes a label map, determines which labels are within a give distance range
    and returns the number of those in a vector.
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    min_distance : float, optional
        default : 0
    max_distance : float, optional
        default: maximum float value
    
    Returns
    -------
    destination
    """
    from .._tier1 import set_column
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier3 import generate_proximal_neighbors_matrix
    from .._tier1 import count_touching_neighbors

    pointlist = centroids_of_labels(source)
    distance_matrix = generate_distance_matrix(pointlist, pointlist)

    touch_matrix = generate_proximal_neighbors_matrix(distance_matrix, min_distance=min_distance, max_distance=max_distance)
    destination = count_touching_neighbors(touch_matrix, destination)
    set_column(destination, 0, 0)
    return destination
