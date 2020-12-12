from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import smaller_or_equal_constant, greater_or_equal_constant, binary_and
from .._tier0 import create_none
from .._tier0 import create_like

@plugin_function(output_creator=create_none)
def exclude_labels_with_values_within_range(values_vector : Image, labels_source : Image, labels_destination : Image = None, min : float = 0, max : float = 100):
    """

    Parameters
    ----------
    values_vector
    labels_source
    labels_destination

    Returns
    -------

    """
    above = create_like(values_vector)
    below = create_like(values_vector)
    flaglist_vector = create_like(values_vector)

    smaller_or_equal_constant(values_vector, below, max)
    greater_or_equal_constant(values_vector, above, min)
    print(below)
    print(above)

    binary_and(below, above, flaglist_vector)
    print(flaglist_vector)

    from .._tier3 import exclude_labels
    labels_destination = exclude_labels(flaglist_vector, labels_source, labels_destination)

    return labels_destination