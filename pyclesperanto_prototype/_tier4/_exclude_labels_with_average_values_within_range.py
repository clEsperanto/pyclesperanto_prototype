import numpy as np

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_labels_like

@plugin_function(output_creator=create_labels_like, categories=['label processing', 'combine', 'in assistant'])
def exclude_labels_with_average_values_within_range(values_image : Image, label_map_input: Image, label_map_destination: Image = None, minimum_value_range : float = 0, maximum_value_range : float = 100) -> Image:
    """This operation removes labels from a labelmap and renumbers the
    remaining labels.

    Parameters
    ----------
    values_image : Image
    label_map_input : Image
    label_map_destination : Image, optional
    minimum_value_range : Number, optional
    maximum_value_range : Number, optional

    Returns
    -------
    label_map_destination

    """
    from .._tier9 import statistics_of_background_and_labelled_pixels
    statistics = statistics_of_background_and_labelled_pixels(values_image, label_map_input)
    values_vector = np.asarray([statistics["mean_intensity"]])
    from .._tier3 import exclude_labels_with_values_within_range

    return exclude_labels_with_values_within_range(values_vector, label_map_input, label_map_destination, minimum_value_range, maximum_value_range)
