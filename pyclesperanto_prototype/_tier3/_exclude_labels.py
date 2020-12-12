from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from .._tier0 import push
from .._tier0 import push_zyx
from .._tier0 import pull
from .._tier0 import create_none
from .._tier0 import create_like
from .._tier1 import replace_intensities
import numpy as np

@plugin_function(output_creator=create_none)
def exclude_labels(flaglist_vector : Image, labels_source : Image, labels_destination : Image = None):
    """

    Parameters
    ----------
    flaglist_vector
    labels_source
    labels_destination

    Returns
    -------

    """
    if labels_destination is None:
        labels_destination = create_like(labels_source)

    num_labels = int(flaglist_vector.shape[-1])

    flaglist_np = pull(flaglist_vector)

    count = 1
    for i in range(1, num_labels):
        if (flaglist_np[i] == 0):
            flaglist_np[i] = count
            count = count + 1
        else:
            flaglist_np[i] = 0

    label_index_map = push(flaglist_np)

    replace_intensities(labels_source, label_index_map, labels_destination)

    return labels_destination