from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_column(output : Image, column : int = 0, scalar : float = 0):
    """Sets all pixel values x of a given column in X to a constant value v.    Parameters
    ----------
    source : Image
    column_index : Number
    value : Number
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set_column(source, column_index, value)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setColumn    

    """


    parameters = {
        "dst":output,
        "column":int(column),
        "value":float(scalar)
    }

    execute(__file__, 'set_column_' + str(len(output.shape)) + 'd_x.cl', 'set_column_' + str(len(output.shape)) + 'd', output.shape, parameters);
    return output
