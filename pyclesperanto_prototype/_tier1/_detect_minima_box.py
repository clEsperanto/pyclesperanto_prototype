from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binarize', 'in assistant'], output_creator=create_binary_like)
def detect_minima_box(source :Image, destination :Image = None, radius_x : int = 0, radius_y : int = 0, radius_z : int = 0):
    """Detects local maxima in a given square/cubic neighborhood. 
    
    Pixels in the resulting image are set to 1 if there is no other pixel in a 
    given radius which has a 
    lower intensity, and to 0 otherwise.
    
    Parameters
    ----------
    source : Image
    destination : Image
    radius_x : Number
    radius_y : Number
    radius_z : Number

    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.detect_minima_box(source, destination, 1, 1, 1)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_detectMaximaBox
    """

    from .._tier0 import create_like
    from .._tier1 import mean_box
    temp = create_like(source)
    mean_box(source, temp, radius_x, radius_y, radius_z)

    parameters = {
        "src":temp,
        "dst":destination
    }

    # todo: ensure detect_minima_2d_x.cl fit to naming convention
    execute(__file__, '../clij-opencl-kernels/kernels/detect_minima_' + str(len(destination.shape)) + 'd_x.cl', 'detect_minima_' + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination
