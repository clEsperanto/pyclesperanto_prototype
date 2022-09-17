from .._tier0 import plugin_function, Image, create_labels_like

@plugin_function(categories=['label processing'], output_creator=create_labels_like)
def merge_labels_according_to_touch_matrix(labels:Image, touch_matrix:Image, labels_destination:Image = None) -> Image:
    """Merge labels in a label image as specified by a binary touch matrix.

    Parameters
    ----------
    labels: Image
    touch_matrix: Image
    labels_destination: Image, optional

    Returns
    -------
    labels_destination
    """


    from .._tier0 import create
    from .._tier1 import multiply_images, set_ramp_y, maximum_y_projection, set_ramp_x, maximum_images, \
        replace_intensities
    from .._tier3 import relabel_sequential
    from .._tier2 import symmetric_maximum_matrix

    # print("touching", touch_matrix[24, 26])
    touch_matrix = symmetric_maximum_matrix(touch_matrix)

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

    # print("li", label_id_vector)
    # print("ol", original_labels)
    # print("nl", new_labels)


    # write the new labels into the label image
    return replace_intensities(labels, new_labels, labels_destination)
