from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_zx

@plugin_function(output_creator=create_2d_zx)
def maximum_y_projection(input : Image, output : Image = None):
    """Determines the maximum intensity projection of an image along X.    Parameters
    ----------
    source : Image
    destination_max : Image
    
    
    Returns
    -------
    destination_max

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.maximum_y_projection(, source, , destination_max)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumYProjection    

    """


    parameters = {
        "dst_max":output,
        "src":input,
    }

    execute(__file__, 'maximum_y_projection_x.cl', 'maximum_y_projection', output.shape, parameters)
    return output
