from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_labels_like

@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def erode_connected_labels(labels_input : Image, labels_destination : Image = None, radius: int = 1) -> Image:
    """Erodes labels to a smaller size. Note: Depending on the label image and the radius,
    labels may disappear and labels may split into multiple islands. Thus, overlapping labels of input and output may
    not have the same identifier.

    Parameters
    ----------
    labels_input : Image
        label image to erode
    labels_destination : Image, optional
        result
    radius : int, optional

    Returns
    -------
    labels_destination

    See Also
    --------
    ..[1] https://clij.github.io/clij2-docs/reference_erodeLabels
    """
    from .._tier1 import greater_constant
    from .._tier1 import copy
    from .._tier1 import multiply_images
    from .._tier3 import relabel_sequential
    from ._erode_labels import erode_labels
    if radius <= 0:
        copy(labels_input, labels_destination)
        return labels_destination

    # binarize
    binary = greater_constant(labels_input, constant=0)

    # erode binary image
    eroded_binary = erode_labels(binary, radius=radius)

    multiplied = multiply_images(labels_input, eroded_binary)
    return relabel_sequential(multiplied, labels_destination)
