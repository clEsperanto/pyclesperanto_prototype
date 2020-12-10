from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from .._tier0 import pull
from .._tier0 import push
from .._tier2 import maximum_of_all_pixels
from .._tier1 import replace_intensities
from .._tier0 import create_like
import numpy as np

@plugin_function
def exclude_labels_on_edges(labels_source : Image, labels_destination : Image = None):
    """
    
    Parameters
    ----------
    labels_source
    labels_destination

    Returns
    -------

    """
    num_labels = int(maximum_of_all_pixels(labels_source))

    label_indices = range(0, num_labels + 1)

    label_index_map = push(np.asarray(label_indices))
    print(label_index_map)

    parameters = {
        "src":labels_source,
        "label_index_dst":label_index_map
    }
    if (len(labels_source.shape) == 3):
        dimensions = [
            labels_source.shape[0],
            labels_source.shape[1],
            labels_source.shape[2]
        ]
    else:
        dimensions = [
            1,
            labels_source.shape[0],
            labels_source.shape[1]
        ]

    if (len(labels_source.shape) == 3):
        global_sizes = [1, dimensions[1], dimensions[2]]
        execute(__file__, "exclude_labels_on_edges_3d_x.cl", "exclude_on_edges_z_3d", global_sizes, parameters)

    global_sizes = [dimensions[0], 1 ,dimensions[2]]
    execute(__file__, "exclude_labels_on_edges_3d_x.cl", "exclude_on_edges_y_3d", global_sizes, parameters)

    global_sizes = [dimensions[0], dimensions[1], 1]
    execute(__file__, "exclude_labels_on_edges_3d_x.cl", "exclude_on_edges_x_3d", global_sizes, parameters)



    label_indices = pull(label_index_map)
    count = 1
    for i in range(1, num_labels + 1):
        if (label_indices[i] > 0):
            label_indices[i] = count
            count = count + 1

    label_index_map = push(np.asarray(label_indices))
    print(label_index_map)


    replace_intensities(labels_source, label_index_map, labels_destination)

    return labels_destination