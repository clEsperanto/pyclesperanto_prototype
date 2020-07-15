from ..tier0 import radius_to_kernel_size
from ..tier0 import execute

def sum_z_projection(input, output):
    """Determines the sum intensity projection of an image along Z.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination_sum)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_sumZProjection


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'sum_z_projection_x.cl', 'sum_z_projection', output.shape, parameters);
