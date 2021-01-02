from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_column(source : Image, column_index : int = 0, value : float = 0):
    """Sets all pixel values x of a given column in X to a constant value v. 
    
    Parameters
    ----------
    source : Image
    column_index : Number
    value : Number
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set_column(source, column_index, value)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_setColumn
    """


    parameters = {
        "dst":source,
        "column":int(column_index),
        "value":float(value)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/set_column_' + str(len(source.shape)) + 'd_x.cl', 'set_column_' + str(len(source.shape)) + 'd', source.shape, parameters);
    return source
