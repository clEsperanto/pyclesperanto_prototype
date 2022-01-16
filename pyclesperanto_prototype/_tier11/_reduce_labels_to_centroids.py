from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import push
from .._tier0 import pull
from .._tier0 import create_like, create_labels_like
from .._tier1 import copy
from .._tier1 import set
import numpy as np

@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def reduce_labels_to_centroids(source:Image, destination:Image=None):
    """Takes a label map and reduces all labels to their center spots. Label IDs stay and background will be zero.

    Parameters
    ----------
    source
    destination

    Returns
    -------
    destination

    See Also
    --------
    ..[0] https://clij.github.io/clij2-docs/reference_reduceLabelsToCentroids
    """
    from .._tier9 import centroids_of_background_and_labels
    from .._tier0 import create
    from .._tier1 import set_ramp_x, set_column, paste, set, write_values_to_positions

    positions = centroids_of_background_and_labels(source)
    positions_and_labels = create((positions.shape[0] + 1, positions.shape[1]))
    set_ramp_x(positions_and_labels)
    set_column(positions, 0, -1)  # prevent putting a 0 at the centroid position of the background
    paste(positions, positions_and_labels, 0, 0)
    set(destination, 0)
    write_values_to_positions(positions_and_labels, destination)

    return destination