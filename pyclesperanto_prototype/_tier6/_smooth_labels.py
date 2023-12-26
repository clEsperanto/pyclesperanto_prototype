from .._tier0 import plugin_function, Image
from .._tier0 import create_labels_like


@plugin_function(categories=['label processing', 'in assistant', 'bia-bob-suggestion'], output_creator=create_labels_like)
def smooth_labels(labels_input: Image, labels_destination: Image = None, radius: int = 0) -> Image:
    """Apply a morphological opening operation to a label image and afterwards
    fills gaps between the labels using voronoi-labeling. Finally, the result
    label image is masked so that all background pixels remain background pixels.

    Note: It is recommended to process isotropic label images.

    Parameters
    ----------
    labels_input: Image
    labels_destination: Image, optional
    radius: int, optional

    Returns
    -------
    labels_destination: Image
    """
    from .._tier1 import greater_constant, multiply_images, copy
    from .._tier4 import extend_labeling_via_voronoi
    from .._tier5 import opening_labels

    if radius < 1:
        return copy(labels_input, labels_destination)

    binary = greater_constant(labels_input, constant=0)

    opened = opening_labels(labels_input, radius=radius)

    extended = extend_labeling_via_voronoi(opened)

    return multiply_images(binary, extended, labels_destination)
