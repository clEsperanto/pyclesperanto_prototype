from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import push
from .._tier0 import pull
from .._tier0 import create_like, create_labels_like
from .._tier1 import copy
from .._tier1 import set
from .._tier1 import onlyzero_overwrite_maximum_box
from .._tier1 import onlyzero_overwrite_maximum_diamond
import numpy as np

@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def extend_labeling_via_voronoi(labeling_source : Image, labeling_destination : Image = None):
    """Takes a label map image and dilates the regions using a octagon shape 
    until they touch. 
    
    The resulting label map is written to the output. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.extend_labeling_via_voronoi(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_extendLabelingViaVoronoi
    """
    flip = create_like(labeling_destination)
    flop = create_like(labeling_destination)

    flag = push(np.asarray([[[0]]]))
    flag_value = 1

    copy(labeling_source, flip)

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
        copy(flip, labeling_destination)
    else:
        copy(flop, labeling_destination)

    return labeling_destination
