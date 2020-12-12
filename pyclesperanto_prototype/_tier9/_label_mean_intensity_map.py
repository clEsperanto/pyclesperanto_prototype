from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push_zyx
from .._tier1 import replace_intensities
from .._tier1 import set_column

@plugin_function
def label_mean_intensity_map(intensity_image : Image, labels : Image, mean_intensity_map : Image = None):
    """

    Parameters
    ----------
    intensity_image
    labels
    mean_intensity_map

    Returns
    -------

    """
    from .._tier9 import statistics_of_background_and_labelled_pixels

    regionprops = statistics_of_background_and_labelled_pixels(intensity_image, labels)

    import numpy as np
    values_vector = push_zyx(np.asarray([[r.mean_intensity for r in regionprops]]))
    set_column(values_vector, 0, 0)

    pixel_count_map = replace_intensities(labels, values_vector)

    return pixel_count_map
