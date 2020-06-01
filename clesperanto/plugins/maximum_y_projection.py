from ..core import radius_to_kernel_size
from ..core import execute

def maximum_y_projection(input, output):
    """
    documentation placeholder
    """


    parameters = {
        "dst_max":output,
        "src":input,
    };

    execute(__file__, 'maximum_y_projection_x.cl', 'maximum_y_projection', output.shape, parameters);
