from ..core import execute

def set(output, scalar):
    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    execute(__file__, 'set_' + str(len(output.shape)) + 'd_x.cl', 'set_' + str(len(output.shape)) + 'd', output.shape, parameters);
