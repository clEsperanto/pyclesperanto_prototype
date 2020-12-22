from .._tier0 import plugin_function
from .._tier0 import create_like
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def gamma_correction(source : Image, target : Image = None, gamma : float = 1):
    """Applies a gamma correction to an image.
    
    Therefore, all pixels x of the Image X are normalized and the power to gamma g is 
    computed, before normlization is reversed (^ is the power 
    operator):f(x) = (x / max(X)) ^ gamma * max(X) 
    
    Parameters
    ----------
    input : Image
    destination : Image
    gamma : Number
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gammaCorrection
    """
    from .._tier1 import multiply_image_and_scalar
    from .._tier1 import power
    from .._tier2 import maximum_of_all_pixels

    max_intensity = maximum_of_all_pixels(source)

    temp1 = create_like(source)
    temp2 = create_like(source)

    multiply_image_and_scalar(source, temp1, 1.0 / max_intensity)
    power(temp1, temp2, gamma)
    multiply_image_and_scalar(temp2, target, max_intensity)

    return target

