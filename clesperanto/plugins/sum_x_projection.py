from ..core import radius_to_kernel_size
from ..core import execute

def sum_x_projection(input, output):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'sum_x_projection_x.cl', 'sum_x_projection', output.shape, parameters);
