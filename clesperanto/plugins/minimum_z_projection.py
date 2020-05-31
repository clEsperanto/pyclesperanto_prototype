from ..core import radius_to_kernel_size
from ..core import execute

def minimum_z_projection(input, output):

    parameters = {
        "dst_min":output,
        "src":input,
    };

    execute(__file__, 'minimum_z_projection_x.cl', 'minimum_z_projection', output.shape, parameters);
