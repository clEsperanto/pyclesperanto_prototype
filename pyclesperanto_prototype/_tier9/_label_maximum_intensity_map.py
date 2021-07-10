from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from .._tier1 import replace_intensities
from .._tier1 import set_column

@plugin_function(categories=['combine', 'label measurement', 'map', 'in assistant'], priority=-1)
def label_maximum_intensity_map(intensity_image : Image, labels : Image, maximum_intensity_map : Image = None):
    """Takes an image and a corresponding label map, determines
    the maximum intensity per label and replaces every label with
    the that number.

    This results in a parametric image expressing maximum object intensity.

    Parameters
    ----------
    intensity_image
    labels
    mean_intensity_map

    Returns
    -------

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumIntensityMap
    """
    from .._tier9 import statistics_of_background_and_labelled_pixels
    from .._tier9 import push_regionprops_column

    regionprops = statistics_of_background_and_labelled_pixels(intensity_image, labels)

    values_vector = push_regionprops_column(regionprops, 'max_intensity')
    set_column(values_vector, 0, 0)

    maximum_intensity_map = replace_intensities(labels, values_vector, maximum_intensity_map)

    return maximum_intensity_map
