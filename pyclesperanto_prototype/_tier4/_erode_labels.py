from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_labels_like

@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def erode_labels(labels_input : Image, labels_destination : Image = None, radius: int = 1, relabel_islands : bool = False):
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
    relabel_islands : Boolean, optional
        True: Make sure that the resulting label image has connected components labeled individually
        and all label indices exist.

    Returns
    -------
    labels_destination

    See Also
    --------
    ..[1] https://clij.github.io/clij2-docs/reference_erodeLabels
    """
    from .._tier1 import copy
    if radius <= 0:
        copy(labels_input, labels_destination)
        return labels_destination

    from .._tier1 import detect_label_edges, binary_not, mask, minimum_sphere, minimum_box, not_equal_constant
    from .._tier3 import relabel_sequential
    from .._tier5 import connected_components_labeling_diamond

    # make a gap between labels == erosion by one pixel
    temp = create_labels_like(labels_input)
    detect_label_edges(labels_input, temp)
    temp1 = binary_not(temp)
    mask(labels_input, temp1, temp)
    del temp1

    if radius == 1:
        copy(temp, labels_destination)
    else:
        for i in range(0, int(radius)):
            if i % 2 == 0:
                minimum_sphere(temp, labels_destination, 1, 1, 1)
            else:
                minimum_box(labels_destination, temp, 1, 1, 1)
    if relabel_islands:
        if radius % 2 == 0:
            copy(temp, labels_destination)
        not_equal_constant(labels_destination, temp)
        connected_components_labeling_diamond(temp, labels_destination)
    else:
        if radius % 2 != 0:
            copy(labels_destination, temp)
        relabel_sequential(temp, labels_destination)

    return labels_destination
