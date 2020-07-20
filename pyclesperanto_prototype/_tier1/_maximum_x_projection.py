from .._tier0 import radius_to_kernel_size
from .._tier0 import execute

def maximum_x_projection(input, output):
    """Determines the maximum projection of an image along X.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination_max)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_maximumXProjection


    Returns
    -------

    """


    parameters = {
        "dst_max":output,
        "src":input,
    };

    execute(__file__, 'maximum_x_projection_x.cl', 'maximum_x_projection', output.shape, parameters);
