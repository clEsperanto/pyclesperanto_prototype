from .._tier0 import create
from .._tier0 import pull
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def minimum_of_all_pixels(source : Image):
    """Determines the minimum of all pixels in a given image. 
    
    It will be stored in a new row of ImageJs
    Results table in the column 'Min'.
    
    Parameters
    ----------
    source : Image
        The image of which the minimum of all pixels or voxels will be determined.
     
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.minimum_of_all_pixels(source)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumOfAllPixels
    """
    from .._tier1 import minimum_x_projection
    from .._tier1 import minimum_y_projection
    from .._tier1 import minimum_z_projection

    dimensionality = source.shape

    if (len(dimensionality) == 3): # 3D image

        temp = create([dimensionality[1], dimensionality[2]])

        minimum_z_projection(source, temp)

        source = temp

        dimensionality = source.shape

    if (len(dimensionality) == 2): # 2D image (or projected 3D)

        temp = create([1, dimensionality[1]])

        minimum_y_projection(source, temp)

        source = temp

    temp = create([1, 1])

    minimum_x_projection(source, temp)

    return pull(temp)[0][0]

