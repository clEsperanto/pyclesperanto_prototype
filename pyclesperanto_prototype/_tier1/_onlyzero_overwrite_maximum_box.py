from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def onlyzero_overwrite_maximum_box(source: Image, flag_dst: Image, destination: Image = None) -> Image:
    """Apply a local maximum filter to an image which only overwrites pixels 
    with value 0. 
    
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
    >>> cle.onlyzero_overwrite_maximum_box(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumBox
    """


    parameters = {
        "dst": destination,
        "flag_dst": flag_dst,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/onlyzero_overwrite_maximum_box_' + str(len(destination.shape)) + 'd_x.cl', 'onlyzero_overwrite_maximum_box_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return [flag_dst, destination]
