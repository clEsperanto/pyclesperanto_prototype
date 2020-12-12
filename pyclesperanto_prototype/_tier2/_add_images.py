from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import add_images_weighted

@plugin_function
def add_images(summand1 : Image, summand2 : Image, destination : Image = None):
    """

    Parameters
    ----------
    summand1
    summand2
    destination

    Returns
    -------

    """
    return add_images_weighted(summand1, summand2, destination, 1, 1)
