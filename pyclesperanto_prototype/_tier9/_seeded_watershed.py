from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_none

@plugin_function(categories=['label', 'combine', 'in assistant'], output_creator=create_none)
def seeded_watershed(distance_map : Image, labelled_spots_seeds : Image, mask : Image = None, labels_destination : Image = None):
    """Seeded watershed implementation from scikit-image [1]

    Parameters
    ----------
    distance_map
    labelled_spots_seeds
    mask
    labels_destination

    Returns
    -------

    See Also
    --------
    .. [1] https://scikit-image.org/docs/dev/api/skimage.segmentation.html?highlight=watershed#skimage.segmentation.watershed
    """
    from .._tier0 import pull_zyx
    from .._tier0 import push_zyx
    from .._tier1 import copy
    from .._tier0 import create_like

    if mask is not None:
        mask = pull_zyx(mask)
    if labelled_spots_seeds is not None:
        labelled_spots_seeds = pull_zyx(labelled_spots_seeds)

    from skimage.segmentation import watershed
    labels = watershed(pull_zyx(distance_map), labelled_spots_seeds, mask=mask)

    if labels_destination == None:
        return push_zyx(labels)
    else:
        temp = push_zyx(labels)
        labels_destination = create_like(temp)
        copy(temp, labels_destination)
        return labels_destination