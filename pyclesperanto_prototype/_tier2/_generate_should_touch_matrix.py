from .._tier0 import create_square_matrix_from_labelmap
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_square_matrix_from_labelmap)
def generate_should_touch_matrix(labels:Image, annotation_binary_mask:Image, destination_touch_matrix:Image=None) -> Image:
    """
    Takes a labelmap with n labels and generates a (n+1)*(n+1) matrix where
    all pixels are set to 0 exept those where labels are marked as touching
    in the annotation_binary_mask. When drawing the annotation_binary_mask,
    make sure to draw so that touching labels receive a value of 1.
    Touching background is ignored.

    Parameters
    ----------
    labels : Image
    annotation_binary_mask: Image
    destination_touch_matrix: Image, optional

    Returns
    -------
    destination_touch_matrix
    """
    from .._tier1 import mask, generate_touch_matrix, set_column, set_row

    masked_labels = mask(labels, annotation_binary_mask)

    generate_touch_matrix(masked_labels, destination_touch_matrix)

    # ignore touching background
    set_column(destination_touch_matrix, 0, 0)
    set_row(destination_touch_matrix, 0, 0)

    return destination_touch_matrix
