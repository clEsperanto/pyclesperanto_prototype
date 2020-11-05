from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_zx

@plugin_function(output_creator=create_2d_zx)
def minimum_y_projection(input : Image, output : Image = None):
    """Determines the minimum intensity projection of an image along Y.    Parameters
    ----------
    source : Image
    destination_sum : Image
    
    
    Returns
    -------
    destination_sum

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumYProjection    

    """


    parameters = {
        "dst_min":output,
        "src":input,
    }

    execute(__file__, 'minimum_y_projection_x.cl', 'minimum_y_projection', output.shape, parameters)
    return output
