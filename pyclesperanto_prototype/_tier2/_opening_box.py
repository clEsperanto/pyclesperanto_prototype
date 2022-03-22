from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function(categories=['filter', 'in assistant'])
def opening_box(input_image: Image, destination: Image = None, radius_x: int = 0, radius_y: int = 0, radius_z: int = 0) -> Image:
    """Opening operator, box-shaped

    Applies morphological opening to intensity images using a box-shaped footprint.
    This operator also works with binary images.

    Parameters
    ----------
    input_image: Image
    destination: Image, optional
    radius_x: int, optional
    radius_y: int, optional
    radius_z: int, optional

    Returns
    -------
    destination
    """
    from .._tier1 import maximum_box, minimum_box
    temp = minimum_box(input_image, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)
    return maximum_box(temp, destination, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)
