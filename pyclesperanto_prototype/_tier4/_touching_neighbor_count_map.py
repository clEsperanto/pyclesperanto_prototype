from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import generate_touch_matrix
from .._tier1 import count_touching_neighbors
from .._tier1 import replace_intensities

@plugin_function(categories=['label measurement', 'map', 'in assistant'], priority=1)
def touching_neighbor_count_map(source : Image, destination : Image = None) -> Image:
    """Takes a label map, determines which labels touch and replaces every 
    label with the number of touching neighboring labels.
    
     
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_touchingNeighborCountMap
    """
    from .._tier1 import set_column

    touch_matrix = generate_touch_matrix(source)
    # ignore how many objects touch the background
    set_column(touch_matrix, 0, 0)

    number_of_touching_neighbors_vector = count_touching_neighbors(touch_matrix)

    replace_intensities(source, number_of_touching_neighbors_vector, destination)
    return destination
