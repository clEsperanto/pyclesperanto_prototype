from ..core import radius_to_kernel_size
from ..core import execute

def sum_y_projection(input, output):

    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'sum_y_projection_x.cl', 'sum_y_projection', output.shape, parameters);
