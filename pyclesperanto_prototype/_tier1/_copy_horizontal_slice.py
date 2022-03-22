from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def copy_horizontal_slice(source : Image, destination : Image = None, slice_index : int = 0) -> Image:
    """This method has two purposes: 
    It copies a 2D image to a given slice y position in a 3D image stack or
    It copies a given slice at position y in an image stack to a 2D image.

    Parameters
    ----------
    source : Image
    destination : Image, optional
    slice_index : Number, optional
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.copy_slice(source, destination, slice_index)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_copySlice
    """


    parameters = {
        "dst":destination,
        "src":source,
        "slice":int(slice_index)
    }

    if (len(destination.shape) == 3):
        execute(__file__, 'copy_horizontal_slice_to_3d_x.cl', 'copy_horizontal_slice_to_3d', [1, source.shape[0], source.shape[1]], parameters)
    else:
        execute(__file__, 'copy_horizontal_slice_from_3d_x.cl', 'copy_horizontal_slice_from_3d', destination.shape, parameters)

    return destination
