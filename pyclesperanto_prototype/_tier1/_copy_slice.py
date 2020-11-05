from .._tier0 import execute


def copy_slice (src, dst, slice):
    """This method has two purposes: 
    It copies a 2D image to a given slice z position in a 3D image stack or 
    It copies a given slice at position z in an image stack to a 2D image.
    
    The first case is only available via ImageJ macro. If you are using it, it is recommended that the 
    target 3D image already pre-exists in GPU memory before calling this method. Otherwise, CLIJ create 
    the image stack with z planes.

    Available for: 3D -> 2D and 2D -> 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number sliceIndex)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_copySlice


    Returns
    -------

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

