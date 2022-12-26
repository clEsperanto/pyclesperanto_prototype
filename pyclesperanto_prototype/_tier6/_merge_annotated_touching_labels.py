from .._tier0 import create_labels_like
from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function(categories=['label processing', 'combine', 'in assistant'], output_creator=create_labels_like)
def merge_annotated_touching_labels(labels:Image, annotation_binary_mask:Image, destination_labels:Image=None) -> Image:
    """
    Takes a labelmap with n labels and merges all objects whose touching
    areas are annotated in a given binary image.
    Touching background is ignored.

    Parameters
    ----------
    labels : Image
    annotation_binary_mask: Image
    destination_labels: Image, optional

    Returns
    -------
    destination_labels
    """
    from .._tier2 import generate_should_touch_matrix
    from .._tier5 import merge_labels_according_to_touch_matrix

    touch_matrix = generate_should_touch_matrix(labels, annotation_binary_mask)
    merge_labels_according_to_touch_matrix(labels, touch_matrix, destination_labels)

    return destination_labels
