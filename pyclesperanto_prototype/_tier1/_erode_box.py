from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def erode_box(src : Image, dst : Image = None):
    """Computes a binary image with pixel values 0 and 1 containing the binary 
    erosion of a given input image. 
    
    The erosion takes the Moore-neighborhood (8 pixels in 2D and 26 pixels in 
    3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be 
    interpreted as 1.
    
    This method is comparable to the 'Erode' menu in ImageJ in case it is 
    applied to a 2D image. The only
    difference is that the output image contains values 0 and 1 instead of 0 and 255. 

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
    >>> cle.erode_box(source, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_erodeBox    

    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'erode_box_' + str(len(dst.shape)) + 'd_x.cl', 'erode_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
