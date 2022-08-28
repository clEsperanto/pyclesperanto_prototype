from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

@plugin_function(categories=['label measurement', 'map', 'in assistant'], priority=1)
def proximal_neighbor_count_map(source : Image, destination : Image = None, min_distance : float = 0, max_distance : float = np.finfo(np.float32).max) -> Image:
    """Takes a label map, determines which labels are within a give distance range
    and replaces every label with the number of neighboring labels.

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
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_proximalNeighborCountMap
    """
    from ._proximal_neighbor_count import proximal_neighbor_count
    from .._tier1 import replace_intensities

    number_of_touching_neighbors_vector = proximal_neighbor_count(source, max_distance=max_distance, min_distance=min_distance)

    replace_intensities(source, number_of_touching_neighbors_vector, destination)
    return destination
