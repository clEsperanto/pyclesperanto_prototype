from .._tier0 import execute

def onlyzero_overwrite_maximum_box (src, flag_dst, dst):
    """Apply a local maximum filter to an image which only overwrites pixels with value 0.    Parameters
    ----------
    input : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.onlyzero_overwrite_maximum_box(input, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumBox    

    """


    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'onlyzero_overwrite_maximum_box_' + str(len(dst.shape)) + 'd_x.cl', 'onlyzero_overwrite_maximum_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
