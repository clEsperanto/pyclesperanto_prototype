from .._tier0 import pull
from .._tier0 import push
from .._tier0 import create_like
from .._tier1 import set
from .._tier1 import set_nonzero_pixels_to_pixelindex
from .._tier1 import nonzero_minimum_box
from .._tier3 import close_index_gaps_in_label_map

import numpy as np

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def connected_components_labeling_box(binary_input : Image, labelmap_output : Image = None):

    """

    :return:
    """

    temp1 = create_like(labelmap_output)
    temp2 = create_like(labelmap_output)

    flag = push(np.asarray([[[0]]]))

    set_nonzero_pixels_to_pixelindex(binary_input, temp1)

    set(temp2, 0)

    flag_value = 1

    iteration_count = 0

    while (flag_value > 0):
        if (iteration_count % 2 == 0):
            nonzero_minimum_box(temp1, flag, temp2)
        else:
            nonzero_minimum_box(temp2, flag, temp1)
        flag_value = pull(flag)[0][0][0]
        iteration_count += 1


    if (iteration_count % 2 == 0):
        close_index_gaps_in_label_map(temp1, labelmap_output)
    else:
        close_index_gaps_in_label_map(temp2, labelmap_output)

    return labelmap_output


