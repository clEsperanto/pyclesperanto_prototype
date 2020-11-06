from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def copy_slice(src : Image, dst : Image = None, slice : int = 0):
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
    sliceIndex : Number
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.copy_slice(source, destination, sliceIndex)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_copySlice    

    """


    parameters = {
        "dst":dst,
        "src":src,
        "slice":int(slice)
    }

    if (len(dst.shape) == 3):
        execute(__file__, 'copy_slice_to_3d_x.cl', 'copy_slice_to_3d', [1, src.shape[0], src.shape[1]], parameters)
    else:
        execute(__file__, 'copy_slice_from_3d_x.cl', 'copy_slice_from_3d', dst.shape, parameters)

    return dst
