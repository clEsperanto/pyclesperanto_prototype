from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def closing_box(input_image: Image, destination: Image = None, radius_x: int = 0, radius_y: int = 0, radius_z: int = 0) -> Image:
    """Closing operator, box-shaped

    Applies morphological closing to intensity images using a box-shaped footprint.
    This operator also works with binary images.

    Parameters
    ----------
    input_image: Image
    destination: Image
    radius_x: int
    radius_y: int
    radius_z: int

    Returns
    -------
    destination
    """
    from .._tier1 import maximum_box, minimum_box
    temp = maximum_box(input_image, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)
    return minimum_box(temp, destination, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)
