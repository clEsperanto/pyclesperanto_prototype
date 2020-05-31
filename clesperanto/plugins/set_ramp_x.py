from ..core import execute

def set_ramp_x(output):
    parameters = {
        "dst":output
    }

    execute(__file__, 'set_ramp_x_' + str(len(output.shape)) + 'd_x.cl', 'set_ramp_x_' + str(len(output.shape)) + 'd', output.shape, parameters);
