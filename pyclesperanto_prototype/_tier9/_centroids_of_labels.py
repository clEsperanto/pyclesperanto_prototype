from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_pointlist_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push

@plugin_function(output_creator=create_pointlist_from_labelmap)
def centroids_of_labels(source:Image, pointlist_destination :Image = None):
    """Determines the centroids of all labels in a label image or image stack. 
    
    It writes the resulting  coordinates in a pointlist image. Depending on 
    the dimensionality d of the labelmap and the number  of labels n, the 
    pointlist image will have n*d pixels. 
    
    Parameters
    ----------
    source : Image
    pointlist_destination : Image
    
    Returns
    -------
    pointlist_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_centroidsOfLabels
    """
    from .._tier9 import statistics_of_labelled_pixels
    regionprops = statistics_of_labelled_pixels(input=None, labelmap=source)

    num_columns = len(source.shape)
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
