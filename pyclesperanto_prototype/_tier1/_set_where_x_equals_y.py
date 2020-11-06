from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_where_x_equals_y(output : Image, scalar : float = 0):
    """Sets all pixel values a of a given image A to a constant value v in 
    case its coordinates x == y. 
    
    Otherwise the pixel is not overwritten.
    If you want to initialize an identity transfrom matrix, set all pixels to 
    0 first. 

    Parameters
    ----------
    source : Image
    value : Number
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setWhereXequalsY    

    """


    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    # todo: rename cl file to fit to naming conventions
    execute(__file__, 'setWhereXequalsY_' + str(len(output.shape)) + 'd_x.cl', 'set_where_x_equals_y_' + str(len(output.shape)) + 'd', output.shape, parameters);
    return output
