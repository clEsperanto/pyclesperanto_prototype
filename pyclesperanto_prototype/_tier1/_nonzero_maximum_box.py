from .._tier0 import execute

def nonzero_maximum_box (src, flag_dst, dst):
    """Apply a maximum filter (box shape) to the input image. 
    
    The radius is fixed to 1 and pixels with value 0 are ignored.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image input, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_nonzeroMaximumBox


    Returns
    -------

    """


    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'nonzero_maximum_box_' + str(len(dst.shape)) + 'd_x.cl', 'nonzero_maximum_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
