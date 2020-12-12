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
def exclude_labels_with_values_out_of_range(values_vector : Image, labels_source : Image, labels_destination : Image = None, min : float = 0, max : float = 100):
    """

    Parameters
    ----------
    values_vector
    labels_source
    labels_destination

    Returns
    -------

    """
    above = create_like(values_vector)
    below = create_like(values_vector)
    flaglist_vector = create_like(values_vector)

    smaller_constant(values_vector, below, min)
    greater_constant(values_vector, above, max)

    binary_or(below, above, flaglist_vector)

    from .._tier3 import exclude_labels
    labels_destination = exclude_labels(flaglist_vector, labels_source, labels_destination)

    return labels_destination