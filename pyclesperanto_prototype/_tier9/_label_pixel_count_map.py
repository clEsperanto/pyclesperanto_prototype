from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from .._tier1 import replace_intensities
from .._tier1 import set_column

@plugin_function(categories=['label measurement', 'map', 'in assistant'])
def label_pixel_count_map(input : Image, destination : Image = None):
    """Takes a label map, determines the number of pixels per label and 
    replaces every label with the that number.
    
    This results in a parametric image expressing area or volume. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_pixelCountMap
    """
    from .._tier9 import statistics_of_background_and_labelled_pixels
    from .._tier9 import push_regionprops_column

    regionprops = statistics_of_background_and_labelled_pixels(None, input)
    values_vector = push_regionprops_column(regionprops, 'area')

    set_column(values_vector, 0, 0)

    destination = replace_intensities(input, values_vector, destination)

    return destination
