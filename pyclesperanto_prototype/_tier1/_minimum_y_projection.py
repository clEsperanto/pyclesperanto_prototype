from .._tier0 import radius_to_kernel_size
from .._tier0 import execute

def minimum_y_projection(input, output):
    """Determines the minimum projection of an image along Y.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination_sum)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_minimumYProjection


    Returns
    -------

    """


    parameters = {
        "dst_min":output,
        "src":input,
    }

    execute(__file__, 'minimum_y_projection_x.cl', 'minimum_y_projection', output.shape, parameters)
