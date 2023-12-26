from .._tier0 import execute

from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function(categories=['combine', 'bia-bob-suggestion'])
def modulo_images(image1 : Image, image2 : Image, destination : Image = None) -> Image:
    """Computes the remainder of a division of pairwise pixel values in two images

    Parameters
    ----------
    image1 : Image
    image2 : Image
    destination : Image, optional

    Returns
    -------
    destination
    """


    parameters = {
        "src":image1,
        "src1":image2,
        "dst": destination
    }

    execute(__file__, 'modulo_images.cl', 'modulo_images', destination.shape, parameters)

    return destination