import numpy as np
from .._tier0 import Image


def n_nearest_labels_to_networkx(label_image: Image, n: int = 1):
    """
    Takes a label image, determines which n labels are the nearest to each label returns an networkx graph
    representing labels in range.

    Parameters
    ----------
    label_image : Image
    n : int, optional
        number of nearest labels

    Returns
    -------
    networkx Graph
    """
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier3 import generate_n_nearest_neighbors_matrix
    from ._to_networkx import to_networkx

    centroids = centroids_of_labels(label_image)
    distance_matrix = generate_distance_matrix(centroids, centroids)
    n_nearest_neighbor_matrix = generate_n_nearest_neighbors_matrix(distance_matrix, n=n)
    return to_networkx(n_nearest_neighbor_matrix, centroids)