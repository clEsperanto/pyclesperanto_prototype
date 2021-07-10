from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from .._tier1 import replace_intensities
from .._tier1 import set_column

@plugin_function(categories=['label measurement', 'map', 'in assistant'])
def label_mean_extension_map(labels : Image, destination : Image = None):
    """Takes a label map, determines for every label the mean
    distance of any pixel to the centroid and replaces every
    label with the that number.
    
    Parameters
    ----------
    labels : Image
    destination : Image
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanExtensionMap
    """
    from .._tier9 import statistics_of_background_and_labelled_pixels
    from .._tier9 import push_regionprops_column

    regionprops = statistics_of_background_and_labelled_pixels(None, labels)
    values_vector = push_regionprops_column(regionprops, 'mean_distance_to_centroid')

    set_column(values_vector, 0, 0)

    destination = replace_intensities(labels, values_vector, destination)

    return destination
