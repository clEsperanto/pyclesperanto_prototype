from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_labels_like

@plugin_function(output_creator=create_labels_like, categories=['label processing', 'combine', 'in assistant'])
def exclude_labels_with_map_values_within_range(values_map : Image, label_map_input: Image, label_map_destination: Image = None, minimum_value_range : float = 0, maximum_value_range : float = 100) -> Image:
    """This operation removes labels from a labelmap and renumbers the
    remaining labels.

    Parameters
    ----------
    values_map : Image
    label_map_input : Image
    label_map_destination : Image
    minimum_value_range : Number
    maximum_value_range : Number

    Returns
    -------
    label_map_destination

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_excludeLabelsWithValuesWithinRange
    """
    from .._tier1 import read_intensities_from_map
    values_vector = read_intensities_from_map(label_map_input, values_map)
    from .._tier3 import exclude_labels_with_values_within_range

    return exclude_labels_with_values_within_range(values_vector, label_map_input, label_map_destination, minimum_value_range, maximum_value_range)
