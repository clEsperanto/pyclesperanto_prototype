from ..core import radius_to_kernel_size
from ..core import execute

def mean_z_projection(input, output):

    parameters = {
        "dst":output,
        "src":input,
    };

    execute(__file__, 'mean_z_projection_x.cl', 'mean_z_projection', output.shape, parameters);
