from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_none
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push

@plugin_function(output_creator=create_none)
def centroids_of_labels(source:Image, pointlist_destination :Image = None, include_background :bool = False, regionprops : list = None):
    """Determines the centroids of all labels in a label image or image stack. 
    
    It writes the resulting  coordinates in a pointlist image. Depending on 
    the dimensionality d of the labelmap and the number  of labels n, the 
    pointlist image will have n*d pixels. 
    
    Parameters
    ----------
    source : Image
    pointlist_destination : Image
    include_background : bool
    regionprops : list of skimage.measure._regionprops.RegionProperties
    
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
    from .._tier1 import copy

    if regionprops is None:
        if include_background:
            regionprops = statistics_of_background_and_labelled_pixels(input=None, labelmap=source, measure_shape=False)
        else:
            regionprops = statistics_of_labelled_pixels(input=None, labelmap=source)

    if hasattr(regionprops[0], 'original_label'):
        labels = [r.original_label for r in regionprops]
    else:
        labels = [r.label for r in regionprops]
    import numpy as np
    max_label = np.max(labels)

    if include_background:
        num_rows = max_label + 1
    else:
        num_rows = max_label

    num_columns = len(source.shape)

    import numpy as np
    matrix = np.zeros([num_rows, num_columns])

    for label_props in regionprops:
        if hasattr(label_props, 'original_label'):
            index = label_props.original_label
        else:
            index = label_props.label

        if not include_background:
            index = index - 1

        # centroid
        if (len(label_props.centroid) == 3):
            matrix[index][0] = label_props.centroid[2]
            matrix[index][1] = label_props.centroid[1]
            matrix[index][2] = label_props.centroid[0]
        else:
            matrix[index][0] = label_props.centroid[1]
            matrix[index][1] = label_props.centroid[0]

    if pointlist_destination is None:
        return push(matrix)
    else:
        temp = push(matrix)
        copy(temp, pointlist_destination)
        return pointlist_destination
