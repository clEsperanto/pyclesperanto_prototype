from .._tier0 import pull
from .._tier0 import push
from .._tier0 import create_like, create_labels_like
from .._tier1 import set
from .._tier1 import set_non_zero_pixels_to_pixel_index
from .._tier1 import nonzero_minimum_box
from .._tier1 import nonzero_minimum_diamond
from .._tier3 import relabel_sequential

import numpy as np

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['label', 'in assistant'], priority=1, output_creator=create_labels_like)
def connected_components_labeling_box(binary_input : Image, labeling_destination : Image = None, flagged_nonzero_minimum_filter : callable = nonzero_minimum_box):
    """Performs connected components analysis inspecting the box neighborhood 
    of every pixel to a binary image and generates a label map. 
    
    Parameters
    ----------
    binary_input : Image
    labeling_destination : Image
    
    Returns
    -------
    labeling_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.connected_components_labeling_box(binary_input, labeling_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_connectedComponentsLabelingBox
    """

    temp1 = create_like(labeling_destination)
    temp2 = create_like(labeling_destination)

    flag = push(np.asarray([[[0]]]))

    set_non_zero_pixels_to_pixel_index(binary_input, temp1)

    set(temp2, 0)

    flag_value = 1

    iteration_count = 0

    while (flag_value > 0):
        if (iteration_count % 2 == 0):
            flagged_nonzero_minimum_filter(temp1, flag, temp2)
        else:
            flagged_nonzero_minimum_filter(temp2, flag, temp1)
        flag_value = pull(flag)[0][0][0]
        set(flag, 0)
        iteration_count += 1

    if (iteration_count % 2 == 0):
        relabel_sequential(temp1, labeling_destination)
    else:
        relabel_sequential(temp2, labeling_destination)

    return labeling_destination
