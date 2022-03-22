from .._tier0 import plugin_function, Image
from .._tier0 import create_like, create_labels_like
from .._tier1 import erode_sphere, erode_box, multiply_images, copy
from .._tier4 import dilate_labels, erode_labels


@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def opening_labels(labels_input: Image, labels_destination: Image = None, radius: int = 0) -> Image:
    """Apply a morphological opening operation to a label image.

    The operation consists of iterative erosion and dilation of the labels.
    With every iteration, box and diamond/sphere structuring elements are used
    and thus, the operation has an octagon as structuring element.

    Parameters
    ----------
    labels_input: Image
    labels_destination: Image, optional
    radius: int, optional

    Returns
    -------
    labels_destination: Image
    """
    if radius == 0:
        return copy(labels_input, labels_destination)

    temp = erode_labels(labels_input, radius=radius)
    return dilate_labels(temp, labels_destination, radius=radius)