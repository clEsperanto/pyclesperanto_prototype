from ..core import execute

def set_image_borders(output, scalar):
    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    execute(__file__, 'set_image_borders_' + str(len(output.shape)) + 'd_x.cl', 'set_image_borders_' + str(len(output.shape)) + 'd', output.shape, parameters);
