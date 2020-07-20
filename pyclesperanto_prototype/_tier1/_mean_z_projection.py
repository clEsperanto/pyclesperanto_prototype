from .._tier0 import radius_to_kernel_size
from .._tier0 import execute

def mean_z_projection(input, output):
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
    };

    execute(__file__, 'mean_z_projection_x.cl', 'mean_z_projection', output.shape, parameters);
