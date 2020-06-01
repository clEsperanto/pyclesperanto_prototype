from ..core import execute


def add_image_and_scalar(input, output, scalar):
    """
    documentation placeholder
    """


    parameters = {
        "src":input,
        "dst":output,
        "scalar":float(scalar)
    };
    execute(__file__, 'add_image_and_scalar_' + str(len(output.shape)) + 'd_x.cl', 'add_image_and_scalar_' + str(len(output.shape)) + 'd', output.shape, parameters);
