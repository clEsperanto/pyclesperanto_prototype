from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier1 import gaussian_blur
from pyclesperanto_prototype._tier0 import create_like
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier2 import subtract_images

@plugin_function
def divide_by_gaussian_background(input : Image, destination : Image = None, sigma_x : float = 2, sigma_y : float = 2, sigma_z : float = 2):
    """

    Parameters
    ----------
    input
    destination
    sigma_x
    sigma_y
    sigma_z

    Returns
    -------

    """
    temp1 = create_like(destination)

    gaussian_blur(input, temp1, sigma_x, sigma_y, sigma_z)

    return subtract_images(input, temp1, destination)
