from .._tier0 import execute

def nonzero_minimum_diamond (input, flag_dst, destination):
    """Apply a minimum filter (diamond shape) to the input image. 
    
    The radius is fixed to 1 and pixels with value 0 are ignored.Note: Pixels 
    with 0 value in the input image will not be overwritten in the output image.
    Thus, the result image should be initialized by copying the original image in 
    advance. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.nonzero_minimum_diamond(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_nonzeroMinimumDiamond
    """


    parameters = {
        "dst": destination,
        "flag_dst": flag_dst,
        "src":input,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/nonzero_minimum_diamond_' + str(len(destination.shape)) + 'd_x.cl', 'nonzero_minimum_diamond_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return [flag_dst, destination]
