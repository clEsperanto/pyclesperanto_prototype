from .._tier0 import Image
from .._tier0 import plugin_function


@plugin_function(categories=['label measurement', 'combine', 'map', 'label comparison', 'in assistant'])
def label_nonzero_pixel_count_map(label_map1: Image, label_map2: Image, overlap_count_map_destination: Image = None):
    """
    Takes two label maps, and counts for every label in label map 1 how many pixels are not zero in label map 2.

    The resulting map is generated from the label map 1 by replacing the labels with the respective count.

    Parameters
    ----------
    label_map1 : Image
    label_map2 : Image
    overlap_count_map_destination : Image, optional

    Returns
    -------
    overlap_count_map_destination
    """
    from .._tier1 import set_column
    from .._tier1 import replace_intensities
    from .._tier9 import statistics_of_background_and_labelled_pixels, push_regionprops_column

    binary = label_map2 > 0

    regionprops = statistics_of_background_and_labelled_pixels(binary, label_map1)

    values_vector = push_regionprops_column(regionprops, 'sum_intensity')
    set_column(values_vector, 0, 0)

    replace_intensities(label_map1, values_vector, overlap_count_map_destination)

    return overlap_count_map_destination
