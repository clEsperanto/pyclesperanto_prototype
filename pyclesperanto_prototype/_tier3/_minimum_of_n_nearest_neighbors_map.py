from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

@plugin_function(categories=['combine', 'neighbor', 'map', 'in assistant'])
def minimum_of_n_nearest_neighbors_map(parametric_map : Image, label_map : Image, parametric_map_destination : Image = None, n : int = 1):
    """Takes a label image and a parametric intensity image and will replace each labels value in the parametric image
    by the minimum value of neighboring labels. The distance number of nearest neighbors can be configured.
    Note: Values of all pixels in a label each must be identical.

    Parameters
    ----------
    parametric_map : Image
    label_map : Image
    parametric_map_destination : Image
    n : int
        number of nearest neighbors
    
    Returns
    -------
    parametric_map_destination

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumOfNNearestNeighbors
    """
    from .._tier1 import read_intensities_from_map
    from .._tier2 import minimum_of_touching_neighbors
    from .._tier1 import replace_intensities
    from .._tier1 import set_column
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier3 import generate_n_nearest_neighbors_matrix

    centroids = centroids_of_labels(label_map)

    distance_matrix = generate_distance_matrix(centroids, centroids)

    touch_matrix = generate_n_nearest_neighbors_matrix(distance_matrix, n=n)

    intensities = read_intensities_from_map(label_map, parametric_map)

    new_intensities = minimum_of_touching_neighbors(intensities, touch_matrix)

    set_column(new_intensities, 0, 0)

    parametric_map_destination = replace_intensities(label_map, new_intensities, parametric_map_destination)

    return parametric_map_destination
