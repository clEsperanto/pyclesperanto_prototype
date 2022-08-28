from .._tier0 import create_none

from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

@plugin_function(output_creator=create_none)
def generate_touch_portion_matrix(label_map:Image, touch_portion_matrix_destination:Image = None) -> Image:
    """Take a label image and measure how often labels X and Y touch and divide it by all
    pixels on the object's border, excluding the image border.
    Put these numbers in a symmetric touch count matrix.

    Note: This matrix is not necessarily symmetric because touch portion depends on the amount
    of label border pixels (divident). Thus, for each edge between labels A and B, two number
    exist: one ratio to label A and one ratio to label B.

    Parameters
    ----------
    label_map: Image
    touch_portion_matrix_destination: Image, optional

    Returns
    -------
    touch_count_matrix_destination
    """
    from .._tier0 import create_like
    from .._tier3 import generate_touch_count_matrix
    from .._tier1 import sum_y_projection
    from .._tier1 import divide_images

    touch_count_matrix = generate_touch_count_matrix(label_map)

    if touch_portion_matrix_destination is None:
        touch_portion_matrix_destination = create_like(touch_count_matrix)

    vector = sum_y_projection(touch_count_matrix)

    return divide_images(touch_count_matrix, vector, touch_portion_matrix_destination)

