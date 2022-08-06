from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import add_images_weighted

@plugin_function(categories=['combine', 'in assistant'], priority=-1)
def clip(source : Image, destination : Image = None, a_min:float = None, a_max:float = None) -> Image:
    """Limits the range of values in an image.

    This function is supposed to work similarly as its counter part in numpy [1].
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    a_min: float, optional
        new, lower limit of the intensity range
    a_max: float, optional
        new, upper limit of the intensity range

    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://numpy.org/doc/stable/reference/generated/numpy.clip.html
    """
    from .._tier1 import maximum_image_and_scalar
    from .._tier1 import minimum_image_and_scalar
    from .._tier1 import copy
    if a_min is not None:
        temp = maximum_image_and_scalar(source, scalar=a_min)
    else:
        temp = source

    if a_max is not None:
        minimum_image_and_scalar(temp, destination, scalar=a_max)
    else:
        copy(temp, destination)

    return destination
