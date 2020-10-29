from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_zy

@plugin_function(output_creator=create_2d_zy)
def sum_x_projection(input : Image, output : Image = None):
    """Determines the sum intensity projection of an image along Z.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_sumXProjection


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "src":input,
    }

    execute(__file__, 'sum_x_projection_x.cl', 'sum_x_projection', output.shape, parameters)
    return output
