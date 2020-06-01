from ..core import radius_to_kernel_size
from ..core import execute

def maximum_z_projection(input, output):
    """
    documentation placeholder
    """


    parameters = {
        "dst_max":output,
        "src":input,
    };

    execute(__file__, 'maximum_z_projection_x.cl', 'maximum_z_projection', output.shape, parameters);
