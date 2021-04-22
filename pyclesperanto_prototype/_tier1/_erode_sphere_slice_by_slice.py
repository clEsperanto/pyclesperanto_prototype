from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binary processing'], output_creator=create_binary_like)
def erode_sphere_slice_by_slice(source : Image, destination : Image = None):
    """Computes a binary image with pixel values 0 and 1 containing the binary 
    erosion of a given input image. 
    
    The erosion takes the von-Neumann-neighborhood (4 pixels in 2D and 6 pixels 
    in 3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be 
    interpreted as 1.
    
    This filter is applied slice by slice in 2D. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.erode_sphere_slice_by_slice(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_erodeSphereSliceBySlice
    """


    parameters = {
        "src":source,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/erode_sphere_slice_by_slice_' + str(len(destination.shape)) + 'd_x.cl', 'erode_sphere_slice_by_slice_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
