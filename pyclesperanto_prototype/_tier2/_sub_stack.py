from warnings import warn

from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier1 import copy_slice

@plugin_function(output_creator=create_none, categories=['transform', 'in assistant'])
def sub_stack(source : Image, destination : Image = None, start_z : int = 0, end_z : int = 0):
    """Crops multiple Z-slices of a 3D stack into a new 3D stack.
    
    Parameters
    ----------
    input : Image
    destination : Image
    start_z : Number
    end_z : Number
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_subStack
    """
    dims = source.shape
    num_slices = int(end_z - start_z + 1)
    if num_slices < 1:
        warn("In sub_stack, end_z should be equal or larger than start_z as num slices must be at least 1")
        num_slices = 1

    if len(dims) < 3:
        warn("A 2D image was passed to sub_stack, which is meant to process 3D images. It will just be copied.")
        from .._tier1 import copy
        return copy(source, destination)

    if destination is None:
        destination = create([num_slices, dims[1], dims[2]])

    from .._tier1 import crop
    crop(source, destination, start_z=start_z, depth=num_slices)

    return destination
