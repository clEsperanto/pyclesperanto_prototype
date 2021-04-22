from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binary processing'], output_creator=create_binary_like)
def dilate_box_slice_by_slice(src : Image, dst : Image = None):
    """Computes a binary image with pixel values 0 and 1 containing the binary 
    dilation of a given input image.
    
    The dilation takes the Moore-neighborhood (8 pixels in 2D and 26 pixels in 
    3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be 
    interpreted as 1.
    
    This method is comparable to the 'Dilate' menu in ImageJ in case it is 
    applied to a 2D image. The only
    difference is that the output image contains values 0 and 1 instead of 0 and 255.
    
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
    >>> cle.dilate_box_slice_by_slice(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_dilateBoxSliceBySlice
    """
    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, '../clij-opencl-kernels/kernels/dilate_box_slice_by_slice_' + str(len(dst.shape)) + 'd_x.cl', 'dilate_box_slice_by_slice_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
