from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def detect_maxima_box(source :Image, destination :Image = None):
    """Detects local maxima in a given square/cubic neighborhood. 
    
    Pixels in the resulting image are set to 1 if there is no other pixel in a 
    given radius which has a 
    higher intensity, and to 0 otherwise. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    radius : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.detect_maxima_box(source, destination, radius)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_detectMaximaBox
    """

    parameters = {
        "src":source,
        "dst":destination
    }

    # todo: ensure detect_maxima_2d_x.cl fit to naming convention
    execute(__file__, 'detect_maxima_' + str(len(destination.shape)) + 'd_x.cl', 'detect_maxima_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination
