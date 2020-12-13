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
def exclude_labels_outside_size_range(input : Image, destination : Image = None, minimum_size : float = 0, maximum_size : float = 100):
    """Removes labels from a label map which are not within a certain size range.
    
    Size of the labels is given as the number of pixel or voxels per label. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    minimum_size : Number
    maximum_size : Number
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    from .._tier9 import statistics_of_background_and_labelled_pixels

    regionprops = statistics_of_background_and_labelled_pixels(None, input)

    values_vector = push_zyx(np.asarray([[r.area for r in regionprops]]))


    above = create_like(values_vector)
    below = create_like(values_vector)
    flaglist_vector = create_like(values_vector)

    smaller_constant(values_vector, below, minimum_size)
    greater_constant(values_vector, above, maximum_size)

    binary_or(below, above, flaglist_vector)

    from .._tier3 import exclude_labels
    destination = exclude_labels(flaglist_vector, input, destination)

    return destination