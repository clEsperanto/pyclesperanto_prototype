from ..core import radius_to_kernel_size
from ..core import execute

def standard_deviation_z_projection(input, output):
    """Determines the standard deviation projection of an image stack along Z.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_standardDeviationZProjection


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'standard_deviation_z_projection_x.cl', 'standard_deviation_z_projection', output.shape, parameters);
