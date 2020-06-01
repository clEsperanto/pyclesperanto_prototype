from ..core import radius_to_kernel_size
from ..core import execute

def minimum_z_projection(input, output):
    """Determines the minimum projection of an image along Z.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination_sum)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_minimumZProjection


    Returns
    -------

    """


    parameters = {
        "dst_min":output,
        "src":input,
    };

    execute(__file__, 'minimum_z_projection_x.cl', 'minimum_z_projection', output.shape, parameters);
