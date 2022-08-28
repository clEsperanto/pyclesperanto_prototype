from .._tier0 import plugin_function
from .._tier1 import replace_intensities
from .._tier0 import Image

@plugin_function(categories=['label measurement', 'in assistant'])
def standard_deviation_touch_portion_map(labels : Image, std_touch_portion_map_destination : Image = None) -> Image:
    """Measure touch portion of all labels to each other and determine the standard deviation of the touch portion for
    each label and write it into a map.

    Parameters
    ----------
    labels: Image
    std_touch_portion_map_destination: Image, optional

    Returns
    -------
    std_touch_portion_map_destination
    """
    from .._tier11 import standard_deviation_touch_portion
    from .._tier1 import replace_intensities
    # save result into a map
    std_touch_portion = standard_deviation_touch_portion(labels)
    return replace_intensities(labels, std_touch_portion, std_touch_portion_map_destination)
