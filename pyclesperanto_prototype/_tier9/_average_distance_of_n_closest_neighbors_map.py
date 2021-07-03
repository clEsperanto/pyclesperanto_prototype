from .._tier0 import plugin_function
from .._tier1 import average_distance_of_n_shortest_distances
from .._tier1 import replace_intensities
from .._tier0 import Image

@plugin_function(categories=['label measurement', 'map', 'in assistant'])
def average_distance_of_n_closest_neighbors_map(labels : Image, distance_map : Image = None, n : int = 1):
    """Takes a label map, determines distances between all centroids and 
    replaces every label with the average distance to the n closest 
    neighboring labels. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    n : Number
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_averageDistanceOfNClosestNeighborsMap
    """

    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix

    centroids = centroids_of_labels(labels)
    distance_matrix = generate_distance_matrix(centroids,centroids)

    value_vector = average_distance_of_n_shortest_distances(distance_matrix, n=n)

    distance_map = replace_intensities(labels, value_vector, distance_map)
    return distance_map

