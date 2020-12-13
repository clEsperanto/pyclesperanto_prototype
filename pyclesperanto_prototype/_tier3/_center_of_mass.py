from .._tier0 import create_like
from .._tier1 import multiply_image_and_coordinate
from .._tier2 import sum_of_all_pixels
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def center_of_mass(source : Image):
    """Determines the center of mass of an image or image stack. 
    
    It writes the result in the results table
    in the columns MassX, MassY and MassZ. 
    
    Parameters
    ----------
    source : Image
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.center_of_mass(source)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_centerOfMass
    """

    temp = create_like(source)

    sum = sum_of_all_pixels(source)

    multiply_image_and_coordinate(source, temp, 0)
    sum_x = sum_of_all_pixels(temp)

    multiply_image_and_coordinate(source, temp, 1)
    sum_y = sum_of_all_pixels(temp)

    multiply_image_and_coordinate(source, temp, 2)
    sum_z = sum_of_all_pixels(temp)

    return [sum_x / sum, sum_y / sum, sum_z / sum]

