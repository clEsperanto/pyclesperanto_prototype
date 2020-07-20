from .._tier0 import execute

def set_where_x_smaller_than_y(output, scalar):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    # todo: rename cl file to fit to naming conventions
    execute(__file__, 'setWhereXsmallerThanY_' + str(len(output.shape)) + 'd_x.cl', 'set_where_x_smaller_than_y_' + str(len(output.shape)) + 'd', output.shape, parameters);
