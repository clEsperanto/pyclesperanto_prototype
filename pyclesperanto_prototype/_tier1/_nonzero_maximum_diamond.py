from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def nonzero_maximum_diamond(source: Image, flag_dst: Image, destination: Image = None) -> Image:
    """Apply a maximum filter (diamond shape) to the input image. 
    
    The radius is fixed to 1 and pixels with value 0 are ignored.
    Note: Pixels with 0 value in the input image will not be overwritten in the 
    output image.
    Thus, the result image should be initialized by copying the original image in 
    advance. 
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.nonzero_maximum_diamond(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_nonzeroMaximumDiamond
    """


    parameters = {
        "dst": destination,
        "flag_dst": flag_dst,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/nonzero_maximum_diamond_' + str(len(destination.shape)) + 'd_x.cl', 'nonzero_maximum_diamond_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return [flag_dst, destination]
