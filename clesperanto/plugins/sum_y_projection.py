from ..core import radius_to_kernel_size
from ..core import execute

def sum_y_projection(input, output):
    """Determines the sum intensity projection of an image along Z.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_sumYProjection


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'sum_y_projection_x.cl', 'sum_y_projection', output.shape, parameters);
