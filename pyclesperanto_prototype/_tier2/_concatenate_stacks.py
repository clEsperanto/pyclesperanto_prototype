from .._tier0 import plugin_function
from .._tier0 import create
from .._tier0 import create_none
from .._tier0 import Image
from .._tier1 import paste

@plugin_function(output_creator=create_none, categories=['combine', 'transform', 'in assistant'])
def concatenate_stacks(stack1 : Image, stack2 : Image, destination : Image = None):
    """Concatenates two stacks in Z. 
    
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
    .. [1] https://clij.github.io/clij2-docs/reference_concatenateStacks
    """

    import numpy as np
    dimensions = np.asarray(stack1.shape)

    if destination is None:
        dimensions[0] = dimensions[0] + stack2.shape[0]

        destination = create(dimensions)

    paste(stack1, destination, 0, 0, 0)
    paste(stack2, destination, 0, 0, stack1.shape[0])

    return destination
