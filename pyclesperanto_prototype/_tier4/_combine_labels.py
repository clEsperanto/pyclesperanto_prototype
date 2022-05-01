from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_labels_like

@plugin_function(categories=['label processing', 'combine labels', 'in assistant'], output_creator=create_labels_like)
def combine_labels(labels_input1 : Image, labels_input2 : Image, labels_destination : Image = None) -> Image:
    """Combines two label images by adding labels of a given label image to another. Labels in the second image
    overwrite labels in the first passed image. Afterwards, labels are relabeled sequentially.

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
    from .._tier1 import greater_constant
    from .._tier1 import maximum_images
    from .._tier2 import maximum_of_all_pixels
    from .._tier1 import add_image_and_scalar
    from .._tier1 import mask
    from .._tier3 import relabel_sequential

    max_labels_1 = maximum_of_all_pixels(labels_input1)

    temp = add_image_and_scalar(labels_input2, scalar=max_labels_1)
    binary = greater_constant(labels_input2, constant=0)

    masked = mask(temp, binary)

    combined = maximum_images(labels_input1, masked)

    return relabel_sequential(combined, labels_destination)