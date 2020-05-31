from ..core import radius_to_kernel_size
from ..core import execute

def maximum_x_projection(input, output):

    parameters = {
        "dst_max":output,
        "src":input,
    };

    execute(__file__, 'maximum_x_projection_x.cl', 'maximum_x_projection', output.shape, parameters);
