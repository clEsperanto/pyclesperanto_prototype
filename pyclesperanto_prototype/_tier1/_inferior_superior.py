from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binary processing'], output_creator=create_binary_like)
def inferior_superior(source : Image, destination : Image = None) -> Image:
    """Dilates the image respectively with a number of kernels and takes the minimum
    value across all results for each pixel.
    
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
    >>> cle.inferior_superior(source, destination)
    
    References
    ----------
    Implemented in inf_sup function in scikit morphological snakes:
    .. [1] https://github.com/scikit-image/scikit-image/blob/00177e14097237ef20ed3141ed454bc81b308f82/skimage/segmentation/morphsnakes.py
    """
    import numpy as np
    if source.dtype != np.uint8:
        # the read function in the kernel below is custom and only supports images of type uint8
        source = source.astype(np.uint8)

    parameters = {
        "src":source,
        "dst":destination
    }

    execute(__file__, './inferior_superior_' + str(len(destination.shape)) + 'd_x.cl', 'inferior_superior_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
