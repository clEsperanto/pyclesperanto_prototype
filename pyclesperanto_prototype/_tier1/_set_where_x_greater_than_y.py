from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_where_x_greater_than_y(output : Image, scalar : float = 0):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    # todo: rename cl file to fit to naming conventions
    execute(__file__, 'setWhereXgreaterThanY_' + str(len(output.shape)) + 'd_x.cl', 'set_where_x_greater_than_y_' + str(len(output.shape)) + 'd', output.shape, parameters);
    return output
