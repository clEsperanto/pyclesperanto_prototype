from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_xy

@plugin_function(output_creator=create_2d_xy)
def mean_z_projection(input : Image, output : Image):
    """Determines the mean average projection of an image along Z.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_meanZProjection


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "src":input,
    }

    execute(__file__, 'mean_z_projection_x.cl', 'mean_z_projection', output.shape, parameters)
    return output
