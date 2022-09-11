from .._tier0 import plugin_function, Image, create_labels_like, create_none
import numpy as np


@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
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
    from .._tier5 import generate_touch_mean_intensity_within_range_matrix

    #print("maximum_intensity", maximum_intensity)
    touch_matrix = generate_touch_mean_intensity_within_range_matrix(image,
                                                                     labels,
                                                                     minimum_intensity=minimum_intensity,
                                                                     maximum_intensity=maximum_intensity)
    # print("touching", touch_matrix[24, 26])

    # vector with 0, 1, 2, 3, ...
    label_id_vector = create([touch_matrix.shape[0], 1])
    set_ramp_y(label_id_vector)

    # multiply vector with touch matrix to get a touch-matrix where
    # labels that should be merged have the value of the "other" label
    touch_matrix = multiply_images(touch_matrix, label_id_vector)

    # the new list of label-IDs for each label is the maximum-y-projection of the matrix
    # if labels 2 and 3 should be merged, both have then label-ID 3
    label_id_vector = create([1, touch_matrix.shape[0]])
    maximum_y_projection(touch_matrix, label_id_vector)

    # replace 0s in this vector with a large number
    # num_labels = labels.max()
    # label_id_vector = cle.replace_intensity(label_id_vector, value_to_replace=0, value_replacement=num_labels)

    # determine minimum of original label versus new label (or large number, in case they should not be merged)
    original_labels = create(label_id_vector.shape)
    set_ramp_x(original_labels)
    # renumber the labels
    new_labels = maximum_images(label_id_vector, original_labels)

    new_labels = relabel_sequential(new_labels)

    #print("li", label_id_vector)
    #print("ol", original_labels)
    #print("nl", new_labels)


    # write the new labels into the label image
    labels_destination = replace_intensities(labels, new_labels, labels_destination)

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
