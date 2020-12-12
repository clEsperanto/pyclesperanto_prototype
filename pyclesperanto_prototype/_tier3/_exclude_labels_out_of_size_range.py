from .._tier0 import plugin_function
from .._tier0 import Image
from .. import smaller_constant, greater_constant, binary_or
from .._tier0 import push
from .._tier0 import push_zyx
from .._tier0 import pull
from .._tier0 import create_none
from .._tier0 import create_like
from .._tier1 import replace_intensities
import numpy as np

@plugin_function(output_creator=create_none)
def exclude_labels_out_of_size_range(labels_source : Image, labels_destination : Image = None, min_size : float = 0, max_size : float = 100):
    """

    Parameters
    ----------
    labels_source
    labels_destination
    min_size
    max_size

    Returns
    -------

    """
    from .._tier9 import statistics_of_background_and_labelled_pixels

    regionprops = statistics_of_background_and_labelled_pixels(None, labels_source)

    values_vector = push_zyx(np.asarray([[r.area for r in regionprops]]))


    above = create_like(values_vector)
    below = create_like(values_vector)
    flaglist_vector = create_like(values_vector)

    smaller_constant(values_vector, below, min_size)
    greater_constant(values_vector, above, max_size)

    binary_or(below, above, flaglist_vector)

    from .._tier3 import exclude_labels
    labels_destination = exclude_labels(flaglist_vector, labels_source, labels_destination)

    return labels_destination