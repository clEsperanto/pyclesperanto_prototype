from ..core import radius_to_kernel_size
from ..core import execute

def sum_z_projection(input, output):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'sum_z_projection_x.cl', 'sum_z_projection', output.shape, parameters);
