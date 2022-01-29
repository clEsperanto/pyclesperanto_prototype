from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import equal_constant
from .._tier0 import create_none
from .._tier0 import create_like

@plugin_function(output_creator=create_none, categories=['label processing', 'combine'])
def exclude_labels_with_values_equal_to_constant(values_vector : Image, label_map_input : Image, label_map_destination : Image = None, constant : float = 0) -> Image:
    """This operation removes labels from a labelmap and renumbers the 
    remaining labels.
    
    Parameters
    ----------
    values_vector : Image
    label_map_input : Image
    label_map_destination : Image
    constant : Number

    Returns
    -------
    label_map_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_excludeLabelsWithValuesWithinRange
    """
    flaglist_vector = create_like(values_vector)

    equal_constant(values_vector, flaglist_vector, constant)

    from .._tier3 import exclude_labels
    label_map_destination = exclude_labels(flaglist_vector, label_map_input, label_map_destination)

    return label_map_destination