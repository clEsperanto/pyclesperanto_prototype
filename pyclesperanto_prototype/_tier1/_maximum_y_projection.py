from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_zx

@plugin_function(output_creator=create_2d_zx)
def maximum_y_projection(input : Image, output : Image = None):
    """Determines the maximum projection of an image along X.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination_max)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_maximumYProjection


    Returns
    -------

    """


    parameters = {
        "dst_max":output,
        "src":input,
    }

    execute(__file__, 'maximum_y_projection_x.cl', 'maximum_y_projection', output.shape, parameters)
    return output
