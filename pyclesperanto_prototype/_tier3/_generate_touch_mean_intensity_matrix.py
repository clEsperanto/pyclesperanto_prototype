import warnings

from .._tier0 import create_none

from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

@plugin_function(output_creator=create_none)
def generate_touch_mean_intensity_matrix(intensity_image:Image, label_map:Image, touch_mean_intensity_matrix_destination:Image = None) -> Image:
    """Take an intensity image and a label image to measure the average intensity along label borders.
    Results are store to a symmetrical matrix.

    Notes
    -----
    * This operation assumes input images are isotropic.
    * The intensity_image should be of integer type. In case of float images, information might be lost.

    Parameters
    ----------
    intensity_image:Image
    label_map: Image
    touch_mean_intensity_matrix_destination: Image, optional

    Returns
    -------
    touch_mean_intensity_matrix_destination
    """
    if intensity_image.dtype not in [np.uint8, np.int8, np.uint16, np.int16, np.uint32, np.int32]:
        warnings.warn("generate_touch_mean_intensity_matrix is supposed to work with images of integer type only.\n" +
                      "Loss of information is possible when passing non-integer images.")

    from .._tier0 import create, execute
    from .._tier1 import set
    from .._tier2 import maximum_of_all_pixels
    from .._tier1 import divide_images

    num_labels = maximum_of_all_pixels(label_map)

    size = (int(num_labels) + 1, int(num_labels) + 1)

    touch_count = create(size, dtype=np.uint32)
    touch_intensity_sum = create(size, dtype=np.uint32)
    set(touch_count, 0)
    set(touch_intensity_sum, 0)

    parameters = {
        "dst_neighbor_touching_count_matrix": touch_count,
        "dst_neighbor_touching_sum_intensity_matrix": touch_intensity_sum,
        "src_label": label_map,
        "src_intensity": intensity_image
    }

    execute(__file__,
            "generate_touch_intensity_matrix.cl",
            "generate_touch_intensity_matrix",
            label_map.shape,
            parameters)

    #print("lm\n", label_map)
    #print("ii\n", intensity_image)
    #print("tc\n", touch_count)
    #print("tis\n", touch_intensity_sum)

    from .._tier2 import symmetric_sum_matrix
    touch_count = symmetric_sum_matrix(touch_count)
    touch_intensity_sum = symmetric_sum_matrix(touch_intensity_sum)

    #print("s tc\n", touch_count)
    #print("s tis\n", touch_intensity_sum)

    if touch_mean_intensity_matrix_destination is None:
        touch_mean_intensity_matrix_destination = create(size)

    return divide_images(touch_intensity_sum, touch_count, touch_mean_intensity_matrix_destination)
