from .._tier0 import plugin_function
from .._tier0 import create
from .._tier0 import create_none
from .._tier0 import Image
from .._tier1 import paste

@plugin_function(output_creator=create_none, categories=['combine', 'transform', 'in assistant'])
def combine_vertically(stack1 : Image, stack2 : Image, destination : Image = None):
    """Combines two images or stacks in Y. 
    
    Parameters
    ----------
    stack1 : Image
    stack2 : Image
    destination : Image
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_combineVertically
    """

    import numpy as np
    dimensions = np.asarray(stack1.shape)

    if destination is None:
        if (len(dimensions) == 3):
            dimensions[1] = dimensions[1] + stack2.shape[1]
        else:
            dimensions[0] = dimensions[0] + stack2.shape[0]

        destination = create(dimensions)

    paste(stack1, destination, 0, 0, 0)
    paste(stack2, destination, 0, stack1.shape[-2], 0)

    return destination
