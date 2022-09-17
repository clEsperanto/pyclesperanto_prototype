from .._tier0 import plugin_function, Image, create_labels_like

@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def merge_small_touching_labels(labels:Image, labels_destination:Image=None, maximum_pixel_count: int = 1000):
    """Merges labels depending on their total volume.

    Note
    ----
    * This algorithm might depend on label order. If there are three touching labels with multiple pairs
      of them below the maximum pixel count, it cannot be garanteed which labels get merged.

    Parameters
    ----------
    labels:Image
    labels_destination:Image, optional
    maximum_pixel_count:int, optional

    Returns
    -------
    labels_destination
    """
    from .._tier1 import copy
    from .._tier2 import sum_of_all_pixels
    from .._tier5 import merge_labels_according_to_touch_matrix

    binary_merge_matrix = _generate_sum_size_matrix_touching_below_threshold(labels, maximum_pixel_count)
    labels_destination = merge_labels_according_to_touch_matrix(labels, binary_merge_matrix, labels_destination)

    binary_merge_matrix = _generate_sum_size_matrix_touching_below_threshold(labels_destination, maximum_pixel_count)

    if sum_of_all_pixels(binary_merge_matrix) > 0:
        # print("nm", new_matrix)
        copied = copy(labels_destination)
        return merge_small_touching_labels(copied, labels_destination,
                                           maximum_pixel_count=maximum_pixel_count)

    return labels_destination


def _generate_sum_size_matrix(labels):
    from .._tier0 import create
    from .._tier1 import transpose_xy
    from .._tier2 import prefix_in_x, add_images
    from .._tier9 import statistics_of_labelled_pixels
    stats = statistics_of_labelled_pixels(labels, labels)
    sizes_x = prefix_in_x([stats["area"]])
    sizes_y = transpose_xy(sizes_x)

    sum_size_matrix = create((sizes_x.shape[1], sizes_x.shape[1]))
    add_images(sizes_x, sizes_y, sum_size_matrix)
    return sum_size_matrix


def _generate_sum_size_matrix_touching_below_threshold(labels, maximum_pixel_count):
    from .._tier1 import generate_touch_matrix, mask, set_row, set_column, set_where_x_equals_y
    sum_size_matrix = _generate_sum_size_matrix(labels)
    touch_matrix = generate_touch_matrix(labels)
    binary_merge_matrix = mask(sum_size_matrix <= maximum_pixel_count, touch_matrix)

    set_column(binary_merge_matrix, 0, 0)
    set_row(binary_merge_matrix, 0, 0)
    set_where_x_equals_y(binary_merge_matrix, 0)
    return binary_merge_matrix