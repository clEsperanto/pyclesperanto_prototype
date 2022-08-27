from .._tier0 import create_none

from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

@plugin_function(output_creator=create_none)
def generate_touch_count_matrix(label_map:Image, touch_count_matrix_destination:Image = None) -> Image:
    """Take a label image and measure how often labels X and Y touch. Put these numbers in a symmetric
    touch count matrix.

    Parameters
    ----------
    label_map: Image
    touch_count_matrix_destination: Image, optional

    Returns
    -------
    touch_count_matrix_destination
    """

    from .._tier0 import create, execute
    from .._tier1 import set, transpose_xy
    from .._tier2 import maximum_of_all_pixels, add_images

    num_labels = maximum_of_all_pixels(label_map)

    size = (int(num_labels) + 1, int(num_labels) + 1)

    if touch_count_matrix_destination is None:
        touch_count_matrix_destination = create(size, dtype=np.uint32)

    temp1 = create(size, dtype=np.uint32)
    temp2 = create(size, dtype=np.uint32)
    set(temp1, 0)

    parameters = {
        "dst_neighbor_touching_count_matrix": temp1,
        "src_label": label_map
    }

    execute(__file__,
            "generate_touch_count_matrix.cl",
            "generate_touch_count_matrix",
            label_map.shape,
            parameters)
    transpose_xy(temp1, temp2)
    return add_images(temp1, temp2, touch_count_matrix_destination)
