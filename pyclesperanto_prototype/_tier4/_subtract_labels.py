from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_labels_like

@plugin_function(categories=['label processing', 'combine labels', 'in assistant'], output_creator=create_labels_like)
def subtract_labels(labels_input1 : Image, labels_input2 : Image, labels_destination : Image = None) -> Image:
    """Combines two label images by removing all labels of a given label image which also exist in another.
    Labels do not have to fit perfectly, if a single pixel overlaps, the label will be removed.

    Parameters
    ----------
    labels_input1 : Image
        label image to add labels to
    labels_input2 : Image
        label image to add labels from
    labels_destination : Image, optional
        result

    Returns
    -------
    labels_destination
    """
    from .._tier3 import relabel_sequential
    from .._tier1 import generate_binary_overlap_matrix, set_row, set_column
    from .._tier1 import maximum_y_projection
    from .._tier3 import exclude_labels

    overlap = generate_binary_overlap_matrix(labels_input1, labels_input2)

    # ignore overlap with background
    set_row(overlap, 0, 0)
    set_column(overlap, 0, 0)

    labels_to_exclude = maximum_y_projection(overlap)

    combined = exclude_labels(labels_to_exclude, labels_input1)

    return relabel_sequential(combined, labels_destination)
