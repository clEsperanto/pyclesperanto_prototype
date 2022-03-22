from .._tier0 import create
from .._tier1 import minimum_box
from .._tier1 import maximum_box
from .._tier1 import add_images_weighted
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'background removal' ,'in assistant'], priority=-1)
def bottom_hat_box(source : Image, destination : Image = None, radius_x : float = 1, radius_y : float = 1, radius_z : float = 1) -> Image:
    """Apply a bottom-hat filter for background subtraction to the input image.
    
    Parameters
    ----------
    source : Image
        The input image where the background is subtracted from.
    destination : Image, optional
        The output image where results are written into.
    radius_x : Image, optional
        Radius of the background determination region in X.
    radius_y : Image, optional
        Radius of the background determination region in Y.
    radius_z : Image, optional
        Radius of the background determination region in Z.

    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.bottom_hat_box(input, destination, radiusX, radiusY, radiusZ)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_bottomHatBox
    """


    temp1 = create(source.shape)
    temp2 = create(source.shape)

    maximum_box(source, temp1, radius_x, radius_y, radius_z)
    minimum_box(temp1, temp2, radius_x, radius_y, radius_z)
    add_images_weighted(temp2, source, destination, 1, -1)
    return destination