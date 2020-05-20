from ..core import execute

def set(output, scalar):
    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    if (len(output.shape) == 2):
        execute(__file__, 'set_2d_x.cl', 'set_2d', output.shape, parameters);
    else:
        execute(__file__, 'set_3d_x.cl', 'set_3d', output.shape, parameters);
