from ..core import execute


def add_image_and_scalar(input, output, scalar):
    parameters = {
        "src":input,
        "dst":output,
        "scalar":float(scalar)
    };
    if (len(output.shape) == 2):
        execute(__file__, 'add_image_and_scalar_2d_x.cl', 'add_image_and_scalar_2d', output.shape, parameters);
    else:
        execute(__file__, 'add_image_and_scalar_3d_x.cl', 'add_image_and_scalar_3d', output.shape, parameters);
