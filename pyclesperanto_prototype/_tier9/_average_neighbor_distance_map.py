from .._tier0 import plugin_function
from .._tier1 import replace_intensities
from .._tier0 import Image

@plugin_function
def average_neighbor_distance_map(labels : Image, distance_map : Image = None):
    """

    Parameters
    ----------
    labels
    distance_map
    n

    Returns
    -------

    """

    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier1 import generate_touch_matrix
    from .._tier1 import average_distance_of_touching_neighbors

    centroids = centroids_of_labels(labels)
    distance_matrix = generate_distance_matrix(centroids,centroids)
    touch_matrix = generate_touch_matrix(labels)

    value_vector = average_distance_of_touching_neighbors(distance_matrix, touch_matrix)

    distance_map = replace_intensities(labels, value_vector, distance_map)
    return distance_map

