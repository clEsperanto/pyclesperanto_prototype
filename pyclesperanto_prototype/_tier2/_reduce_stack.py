
from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier1 import copy_slice

@plugin_function(output_creator=create_none)
def reduce_stack(stack_input : Image, stack_output : Image = None, factor : int = 2, offset : int = 0):
    """

    Parameters
    ----------
    stack_input
    stack_output
    factor
    offset

    Returns
    -------

    """
    dims = stack_input.shape
    num_slices = int(dims[0] / factor)
    if stack_output is None:
        stack_output = create([num_slices, dims[1], dims[2]])

    slice = create([dims[1], dims[2]])

    for z in range(0, num_slices):
        copy_slice(stack_input, slice, z * factor + offset)
        copy_slice(slice, stack_output, z)

    return stack_output
