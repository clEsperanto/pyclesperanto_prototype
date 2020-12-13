from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push_zyx
from .._tier1 import replace_intensities
from .._tier1 import set_column

@plugin_function
def label_mean_intensity_map(input : Image, label_map : Image, destination : Image = None):
    """Takes an image and a corresponding label map, determines the mean 
    intensity per label and replaces every label with the that number.
    
    This results in a parametric image expressing mean object intensity. 
    
    Parameters
    ----------
    input : Image
    label_map : Image
    destination : Image
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_labelMeanIntensityMap
    """
    from .._tier9 import statistics_of_background_and_labelled_pixels

    regionprops = statistics_of_background_and_labelled_pixels(input, label_map)

    import numpy as np
    values_vector = push_zyx(np.asarray([[r.mean_intensity for r in regionprops]]))
    set_column(values_vector, 0, 0)

    destination = replace_intensities(label_map, values_vector, destination)

    return destination
