from .._tier0 import Image
from .._tier0 import plugin_function


@plugin_function(categories=['label measurement', 'combine', 'map', 'label comparison', 'in assistant'])
def label_overlap_count_map(label_map1: Image, label_map2: Image, overlap_count_map_destination: Image = None):
    """
    Takes two label maps, and counts for every label in label map 1 how many labels overlap with it in label map 2.

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
    from .._tier1 import generate_binary_overlap_matrix
    from .._tier1 import set_row
    from .._tier1 import sum_y_projection
    from .._tier1 import set_column
    from .._tier1 import replace_intensities

    overlap_matrix = generate_binary_overlap_matrix(label_map1, label_map2)

    set_row(overlap_matrix, 0, 0)

    overlap_count_array = sum_y_projection(overlap_matrix)

    set_column(overlap_count_array, 0, 0)

    replace_intensities(label_map1, overlap_count_array, overlap_count_map_destination)

    return overlap_count_map_destination
