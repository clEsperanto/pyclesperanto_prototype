from .._tier0 import execute

def onlyzero_overwrite_maximum_diamond (src, flag_dst, dst):
    """Apply a local maximum filter to an image which only overwrites pixels with value 0.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image input, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumDiamond


    Returns
    -------

    """


    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'onlyzero_overwrite_maximum_diamond_' + str(len(dst.shape)) + 'd_x.cl', 'onlyzero_overwrite_maximum_diamond_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
