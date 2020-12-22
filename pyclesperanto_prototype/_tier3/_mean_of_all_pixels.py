from pyclesperanto_prototype._tier2 import sum_of_all_pixels
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
import numpy as np

@plugin_function
def mean_of_all_pixels(source : Image):
    """Determines the mean average of all pixels in a given image. 
    
    It will be stored in a new row of ImageJs
    Results table in the column 'Mean'.Parameters
    ----------
    source : Image
        The image of which the mean average of all pixels or voxels will be determined.
     
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.mean_of_all_pixels(source)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanOfAllPixels
    """

    num_pixels = np.prod(source.shape)

    return sum_of_all_pixels(source) / num_pixels

