from .._tier0 import plugin_function
from .._tier0 import Image
from .. import smaller_constant, greater_constant, binary_or
from .._tier0 import create_none
from .._tier0 import create_like

@plugin_function(output_creator=create_none, categories=['label processing', 'combine', 'in assistant'])
def exclude_labels_with_values_out_of_range(values_vector : Image, label_map_input : Image, label_map_destination : Image = None, minimum_value_range : float = 0, maximum_value_range : float = 100):
    """This operation removes labels from a labelmap and renumbers the 
    remaining labels. 
    
    Hand over a vector of values and a range specifying which labels with which 
    values are eliminated. 
    
    Parameters
    ----------
    values_vector : Image
    label_map_input : Image
    label_map_destination : Image
    minimum_value_range : Number
    maximum_value_range : Number
    
    Returns
    -------
    label_map_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_excludeLabelsWithValuesOutOfRange
    """
    above = create_like(values_vector)
    below = create_like(values_vector)
    flaglist_vector = create_like(values_vector)

    smaller_constant(values_vector, below, minimum_value_range)
    greater_constant(values_vector, above, maximum_value_range)

    binary_or(below, above, flaglist_vector)

    from .._tier3 import exclude_labels
    label_map_destination = exclude_labels(flaglist_vector, label_map_input, label_map_destination)

    return label_map_destination