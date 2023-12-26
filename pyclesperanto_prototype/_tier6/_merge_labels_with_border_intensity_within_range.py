from .._tier0 import plugin_function, Image, create_labels_like, create_none
import numpy as np


@plugin_function(categories=['label processing', 'in assistant', 'bia-bob-suggestion'], output_creator=create_labels_like)
def merge_labels_with_border_intensity_within_range(image: Image,
                                                    labels: Image,
                                                    labels_destination: Image = None,
                                                    minimum_intensity: float = 0,
                                                    maximum_intensity: float = np.finfo(np.float32).max):
    """Takes an image and a label image to determine the mean intensity along borders between labels. Afterwards,
    it merges labels whose border intensity is within a specified range.

    Notes
    -----
    * For technical reasons, only images of integer type are supported. In case images of type float are passed,
      the results may not be 100% repeatable.
    * The specified range includes minimum and maximum

    Parameters
    ----------
    image: Image
    labels: Image
    labels_destination: Image, optional
    minimum_intensity: float, optional
    maximum_intensity: float, optional

    Returns
    -------
    labels_destination
    """

    from .._tier0 import create
    from .._tier1 import multiply_images, set_ramp_y, maximum_y_projection, set_ramp_x, maximum_images, \
        replace_intensities, copy
    from .._tier2 import sum_of_all_pixels
    from .._tier3 import relabel_sequential
    from .._tier5 import generate_touch_mean_intensity_within_range_matrix, merge_labels_according_to_touch_matrix

    #print("maximum_intensity", maximum_intensity)
    touch_matrix = generate_touch_mean_intensity_within_range_matrix(image,
                                                                     labels,
                                                                     minimum_intensity=minimum_intensity,
                                                                     maximum_intensity=maximum_intensity)

    labels_destination = merge_labels_according_to_touch_matrix(labels, touch_matrix, labels_destination)

    # determine matrix again and see if there is anything to be merged
    new_matrix = generate_touch_mean_intensity_within_range_matrix(image, labels_destination,
                                                                   minimum_intensity=minimum_intensity,
                                                                   maximum_intensity=maximum_intensity)

    if sum_of_all_pixels(new_matrix) > 0:
        #print("nm", new_matrix)
        copied = copy(labels_destination)
        return merge_labels_with_border_intensity_within_range(image, copied, labels_destination,
                                                                   minimum_intensity=minimum_intensity,
                                                                   maximum_intensity=maximum_intensity)
    return labels_destination
