from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_pointlist_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push

@plugin_function(output_creator=create_pointlist_from_labelmap)
def label_centroids_to_pointlist(labels:Image, destination_pointlist :Image = None):
    """
    """
    from .._tier9 import statistics_of_labelled_pixels
    regionprops = statistics_of_labelled_pixels(input_image=None, input_label_map=labels)

    num_columns = len(labels.shape)
    num_rows = len(regionprops)

    import numpy as np
    matrix = np.zeros([num_rows, num_columns])

    for i, label_props in enumerate(regionprops):
        #print(i)
        # centroid
        if (len(label_props.centroid) == 3):
            matrix[i][0] = label_props.centroid[2]
            matrix[i][1] = label_props.centroid[1]
            matrix[i][2] = label_props.centroid[0]
        else:
            matrix[i][0] = label_props.centroid[1]
            matrix[i][1] = label_props.centroid[0]

    return push(matrix)
