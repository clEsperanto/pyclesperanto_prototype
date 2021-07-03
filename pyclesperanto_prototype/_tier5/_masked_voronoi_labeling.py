from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_like, create_labels_like
from .._tier4 import connected_components_labeling_box
from .._tier4 import extend_labeling_via_voronoi

@plugin_function(categories=['label'], output_creator=create_labels_like)
def masked_voronoi_labeling(binary_source : Image, mask_image : Image, labeling_destination : Image = None):
    """Takes a binary image, labels connected components and dilates the
    regions using a octagon shape until they touch. The region growing is limited to a masked area.
    
    The resulting label map is written to the output. 
    
    Parameters
    ----------
    binary_source : Image
    mask_image : Image
    labeling_destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.masked_voronoi_labeling(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maskedVoronoiLabeling
    """

    from .._tier0 import push
    from .._tier0 import pull
    from .._tier0 import create_like
    from .._tier1 import set
    from .._tier1 import onlyzero_overwrite_maximum_box
    from .._tier1 import onlyzero_overwrite_maximum_diamond
    from .._tier1 import add_image_and_scalar
    from .._tier2 import add_images
    from .._tier1 import mask

    flup = create_like(labeling_destination)
    flip = create_like(labeling_destination)
    flop = create_like(labeling_destination)

    import numpy as np

    add_image_and_scalar(mask_image, flup, -1)

    connected_components_labeling_box(binary_source, flop)

    add_images(flup, flop, flip)

    flag = push(np.asarray([[[0]]]))
    flag_value = 1


    iteration_count = 0

    while (flag_value > 0):
        if (iteration_count % 2 == 0):
            onlyzero_overwrite_maximum_box(flip, flag, flop)
        else:
            onlyzero_overwrite_maximum_diamond(flop, flag, flip)
        flag_value = pull(flag)[0][0][0]
        set(flag, 0)
        iteration_count += 1

    if (iteration_count % 2 == 0):
        mask(flip, mask_image, labeling_destination)
    else:
        mask(flop, mask_image, labeling_destination)

    return labeling_destination



