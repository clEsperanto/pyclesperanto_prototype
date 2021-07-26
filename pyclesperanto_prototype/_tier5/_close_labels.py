from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_like, create_labels_like

@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def close_labels(labeling_source : Image, labeling_destination : Image = None, radius: int = 1,
                relabel_islands: bool = False):
    """Closing label images analogously to binary opening. Applies dilate_labels and erode_labels subsequently.
    Note: Depending on the label image and the radius, labels may disappear and labels may split into
    multiple islands. Thus, overlapping labels of input and output may not have the same identifier.

    Parameters
    ----------
    labeling_source: Image
    labeling_destination: Image, optional
    radius: int, optional
    relabel_islands: bool, optional
        True: Make sure that the resulting label image has connected components labeled individually
        and all label indices exist.

    Returns
    -------
    labeling_destination
    """
    from .._tier4 import erode_labels
    from .._tier4 import dilate_labels
    temp = dilate_labels(labeling_source, radius=radius)
    erode_labels(temp, labeling_destination, radius=radius, relabel_islands=relabel_islands)
    return labeling_destination
