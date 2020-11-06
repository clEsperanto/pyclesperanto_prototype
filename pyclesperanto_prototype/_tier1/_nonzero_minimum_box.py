from .._tier0 import execute

def nonzero_minimum_box (src, flag_dst, dst):
    """Apply a minimum filter (box shape) to the input image. 
    
    The radius is fixed to 1 and pixels with value 0 are ignored.
    Note: Pixels with 0 value in the input image will not be overwritten in the 
    output image.
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
    >>> cle.nonzero_minimum_box(input, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_nonzeroMinimumBox    

    """


    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'nonzero_minimum_box_' + str(len(dst.shape)) + 'd_x.cl', 'nonzero_minimum_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
