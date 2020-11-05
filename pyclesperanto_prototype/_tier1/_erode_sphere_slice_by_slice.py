from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def erode_sphere_slice_by_slice(src : Image, dst : Image = None):
    """Computes a binary image with pixel values 0 and 1 containing the binary erosion of a given input image. 
    
    The erosion takes the von-Neumann-neighborhood (4 pixels in 2D and 6 pixels in 3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be interpreted as 1.
    
    This filter is applied slice by slice in 2D.    Parameters
    ----------
    source : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.erode_sphere_slice_by_slice(, source, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_erodeSphereSliceBySlice    

    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'erode_sphere_slice_by_slice_' + str(len(dst.shape)) + 'd_x.cl', 'erode_sphere_slice_by_slice_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
