from ..core import radius_to_kernel_size
from ..core import execute

def standard_deviation_z_projection(input, output):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'standard_deviation_z_projection_x.cl', 'standard_deviation_z_projection', output.shape, parameters);
