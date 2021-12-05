import numpy as np
from .._tier0 import Image

def touching_labels_to_igraph(label_image:Image):
    """
    Takes a label image, determines which labels are touching each other and returns an igraph graph
    representing labels in range.

    Parameters
    ----------
    label_image : Image

    Returns
    -------
    igraph Graph
    """
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_touch_matrix
    from ._to_igraph import to_igraph

    centroids = centroids_of_labels(label_image)
    touch_matrix = generate_touch_matrix(label_image)
    return to_igraph(touch_matrix, centroids)