from .._tier0 import execute

def set_where_x_smaller_than_y(output, scalar):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    execute(__file__, 'set_where_x_smaller_than_y_' + str(len(output.shape)) + 'd_x.cl', 'set_where_x_smaller_than_y_' + str(len(output.shape)) + 'd', output.shape, parameters);
