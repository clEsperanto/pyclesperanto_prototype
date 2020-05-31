from ..core import execute


def subtract_image_from_scalar(input, output, scalar):
    parameters = {
        "src":input,
        "dst":output,
        "scalar":float(scalar)
    };
    execute(__file__, 'subtract_image_from_scalar_' + str(len(output.shape)) + 'd_x.cl', 'subtract_image_from_scalar_' + str(len(output.shape)) + 'd', output.shape, parameters);
