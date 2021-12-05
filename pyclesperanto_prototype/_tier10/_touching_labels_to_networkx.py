import numpy as np
from .._tier0 import Image

def touching_labels_to_networkx(label_image:Image):
    """
    Takes a label image, determines which labels are touching each other and returns an networkx graph
    representing labels in range.

    Parameters
    ----------
    label_image : Image

    Returns
    -------
    networkx Graph
    """
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_touch_matrix
    from ._to_networkx import to_networkx

    centroids = centroids_of_labels(label_image)
    touch_matrix = generate_touch_matrix(label_image)
    return to_networkx(touch_matrix, centroids)