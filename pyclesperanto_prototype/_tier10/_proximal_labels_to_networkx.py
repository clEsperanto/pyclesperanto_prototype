import numpy as np
from .._tier0 import Image

def proximal_labels_to_networkx(label_image:Image, minimum_distance : float = 0, maximum_distance : float = np.finfo(np.float32).max):
    """
    Takes a label image, determines which labels are in a given distance range and returns an networkx graph
    representing labels in range.

    Parameters
    ----------
    label_image : Image
    minimum_distance : float, optional
    maximum_distance : float, optional

    Returns
    -------
    networkx Graph
    """
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier3 import generate_proximal_neighbors_matrix
    from ._to_networkx import to_networkx

    centroids = centroids_of_labels(label_image)
    distance_matrix = generate_distance_matrix(centroids, centroids)
    proximal_matrix = generate_proximal_neighbors_matrix(distance_matrix, min_distance=minimum_distance, max_distance=maximum_distance)
    return to_networkx(proximal_matrix, centroids)
