from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from .._tier0 import push
from .._tier0 import pull
from .._tier0 import create_none
from .._tier0 import create_like, create_labels_like
from .._tier1 import replace_intensities
import numpy as np

@plugin_function(output_creator=create_none)
def exclude_labels(binary_flaglist : Image, label_map_input : Image, label_map_destination : Image = None):
    """This operation removes labels from a labelmap and renumbers the 
    remaining labels. 
    
    Hand over a binary flag list vector starting with a flag for the background, 
    continuing with label1, label2, ...
    
    For example if you pass 0,1,0,0,1: Labels 1 and 4 will be removed (those 
    with a 1 in the vector will be excluded). Labels 2 and 3 will be kept 
    and renumbered to 1 and 2. 
    
    Parameters
    ----------
    binary_flaglist : Image
    label_map_input : Image
    label_map_destination : Image
    
    Returns
    -------
    label_map_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_excludeLabels
    """
    if label_map_destination is None:
        label_map_destination = create_labels_like(label_map_input)

    num_labels = int(binary_flaglist.shape[-1])

    flaglist_np = pull(binary_flaglist)

    flaglist_np[0][0] = 0
    
    count = 1
    for i in range(1, num_labels):
        if (flaglist_np[0][i] == 0):
            flaglist_np[0][i] = count
            count = count + 1
        else:
            flaglist_np[0][i] = 0

    label_index_map = push(flaglist_np)

    replace_intensities(label_map_input, label_index_map, label_map_destination)

    return label_map_destination