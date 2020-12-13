from .._tier0 import create_like
from .._tier1 import multiply_image_and_coordinate
from .._tier2 import maximum_of_all_pixels
from .._tier2 import minimum_of_masked_pixels
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def bounding_box(source : Image):
    """Determines the bounding box of all non-zero pixels in a binary image. 
    
    If called from macro, the positions will be stored in a new row of ImageJs 
    Results table in the columns 'BoundingBoxX', 'BoundingBoxY', 
    'BoundingBoxZ', 'BoundingBoxWidth', 'BoundingBoxHeight' 
    'BoundingBoxDepth'.In case of 2D images Z and depth will be zero. 
    
    Parameters
    ----------
    source : Image
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.bounding_box(source)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_boundingBox
    """

    temp = create_like(source)

    multiply_image_and_coordinate(source, temp, 0)
    max_x = maximum_of_all_pixels(temp)
    min_x = minimum_of_masked_pixels(temp, source)
    print("min_x" + str(min_x))

    multiply_image_and_coordinate(source, temp, 1)
    max_y = maximum_of_all_pixels(temp)
    min_y = minimum_of_masked_pixels(temp, source)

    if len(source.shape) == 3:
        multiply_image_and_coordinate(source, temp, 2)
        max_z = maximum_of_all_pixels(temp)
        min_z = minimum_of_masked_pixels(temp, source)

        return [min_x, min_y, min_z, max_x, max_y, max_z]
    else:
        return [min_x, min_y, 0, max_x, max_y, 0]
