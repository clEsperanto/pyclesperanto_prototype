from .._tier0 import execute

def set_where_x_equals_y(output, scalar):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    # todo: rename cl file to fit to naming conventions
    execute(__file__, 'setWhereXequalsY_' + str(len(output.shape)) + 'd_x.cl', 'set_where_x_equals_y_' + str(len(output.shape)) + 'd', output.shape, parameters);
