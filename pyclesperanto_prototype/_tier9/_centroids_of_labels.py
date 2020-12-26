from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_pointlist_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push

@plugin_function(output_creator=create_pointlist_from_labelmap)
def centroids_of_labels(source:Image, pointlist_destination :Image = None, include_background :bool = False):
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
    from .._tier9 import statistics_of_background_and_labelled_pixels
    from .._tier2 import maximum_of_all_pixels

    if include_background:
        regionprops = statistics_of_background_and_labelled_pixels(input=None, labelmap=source)
        num_rows = int(maximum_of_all_pixels(source) + 1)
    else:
        regionprops = statistics_of_labelled_pixels(input=None, labelmap=source)
        num_rows = int(maximum_of_all_pixels(source))

    num_columns = len(source.shape)
    #num_rows = len(regionprops)

    import numpy as np
    matrix = np.zeros([num_rows, num_columns])

    for i, label_props in enumerate(regionprops):
        index = label_props.label - 1
        print(index)
        # centroid
        if (len(label_props.centroid) == 3):
            matrix[index][0] = label_props.centroid[2]
            matrix[index][1] = label_props.centroid[1]
            matrix[index][2] = label_props.centroid[0]
        else:
            matrix[index][0] = label_props.centroid[1]
            matrix[index][1] = label_props.centroid[0]

    return push(matrix)
