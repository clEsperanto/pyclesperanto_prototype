from pyclesperanto_prototype._tier2 import sum_of_all_pixels
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
import numpy as np

@plugin_function
def mean_of_all_pixels(source : Image):
    """

    Parameters
    ----------
    source

    Returns
    -------

    """

    num_pixels = np.prod(source.shape)

    return sum_of_all_pixels(source) / num_pixels

