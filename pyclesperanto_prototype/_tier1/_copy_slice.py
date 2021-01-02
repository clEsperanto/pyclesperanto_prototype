from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def copy_slice(source : Image, destination : Image = None, slice_index : int = 0):
    """This method has two purposes: 
    It copies a 2D image to a given slice z position in a 3D image stack or 
    It copies a given slice at position z in an image stack to a 2D image.
    
    The first case is only available via ImageJ macro. If you are using it, it 
    is recommended that the 
    target 3D image already pre-exists in GPU memory before calling this method. 
    Otherwise, CLIJ create 
    the image stack with z planes. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    slice_index : Number
    
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
        execute(__file__, '../clij-opencl-kernels/kernels/copy_slice_to_3d_x.cl', 'copy_slice_to_3d', [1, source.shape[0], source.shape[1]], parameters)
    else:
        execute(__file__, '../clij-opencl-kernels/kernels/copy_slice_from_3d_x.cl', 'copy_slice_from_3d', destination.shape, parameters)

    return destination
