from .._tier0 import execute
from .._tier0 import create_2d_xy
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_2d_xy)
def maximum_z_projection(input :Image, output :Image = None):
    """Determines the maximum projection of an image along Z.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination_max)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_maximumZProjection


    Returns
    -------

    """


    parameters = {
        "dst_max":output,
        "src":input,
    }

    execute(__file__, 'maximum_z_projection_x.cl', 'maximum_z_projection', output.shape, parameters)

    return output
