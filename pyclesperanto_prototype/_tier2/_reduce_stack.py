import warnings

from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier1 import copy_slice

@plugin_function(output_creator=create_none, categories=['transform', 'in assistant'])
def reduce_stack(input : Image, destination : Image = None, reduction_factor : int = 2, offset : int = 0):
    """Reduces the number of slices in a stack by a given factor.
    With the offset you have control which slices stay: 
    * With factor 3 and offset 0, slices 0, 3, 6,... are kept. * With factor 
    4 and offset 1, slices 1, 5, 9,... are kept. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    reduction_factor : Number
    offset : Number
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_reduceStack
    """
    dims = input.shape
    if reduction_factor < 1:
        warnings.warn("In sub_stack, reduction_factor must be larger than 0")
        reduction_factor = 1

    num_slices = int(dims[0] / reduction_factor)
    if destination is None:
        destination = create([num_slices, dims[1], dims[2]])

    slice = create([dims[1], dims[2]])

    for z in range(0, num_slices):
        copy_slice(input, slice, z * reduction_factor + offset)
        copy_slice(slice, destination, z)

    return destination
