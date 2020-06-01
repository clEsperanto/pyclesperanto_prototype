from ..core import execute

def set_ramp_y(output):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output
    }

    execute(__file__, 'set_ramp_y_' + str(len(output.shape)) + 'd_x.cl', 'set_ramp_y_' + str(len(output.shape)) + 'd', output.shape, parameters);
