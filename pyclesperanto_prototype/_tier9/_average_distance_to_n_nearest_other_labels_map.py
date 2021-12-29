from .._tier0 import plugin_function
from .._tier1 import replace_intensities
from .._tier0 import Image

@plugin_function(categories=['label measurement', 'map', 'in assistant'])
def average_distance_to_n_nearest_other_labels_map(labels : Image, other_labels : Image, distance_map : Image = None, n : int = 1):
    """Takes two label maps and determines the centroid distances from each label in the first label image
    to the labels in the second. The average distance of the n nearest neighbors is then averaged and
    stored in a parametric distance map image.
    
    Parameters
    ----------
    labels : Image
    other_labels
    distance_map : Image
    n : Number
    
    Returns
    -------
    distance_map
    """

    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier1 import average_distance_of_n_nearest_distances

    centroids_a = centroids_of_labels(labels)
    centroids_b = centroids_of_labels(other_labels)
    distance_matrix = generate_distance_matrix(centroids_a,centroids_b)

    value_vector = average_distance_of_n_nearest_distances(distance_matrix, n=n)

    distance_map = replace_intensities(labels, value_vector, distance_map)
    return distance_map

