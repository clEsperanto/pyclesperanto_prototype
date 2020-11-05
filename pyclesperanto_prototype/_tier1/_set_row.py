from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_row(output : Image, row : int = 0, scalar : float = 0):
    """Sets all pixel values x of a given row in X to a constant value v.    Parameters
    ----------
    source : Image
    row_index : Number
    value : Number
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set_row(source, row_index, value)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setRow    

    """


    parameters = {
        "dst":output,
        "row":int(row),
        "value":float(scalar)
    }

    execute(__file__, 'set_row_' + str(len(output.shape)) + 'd_x.cl', 'set_row_' + str(len(output.shape)) + 'd', output.shape, parameters);
    return output
