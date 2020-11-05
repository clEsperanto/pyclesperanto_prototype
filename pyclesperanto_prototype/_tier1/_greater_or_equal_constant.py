from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def greater_or_equal_constant(src1 : Image, dst : Image = None, scalar : float = 0):
    """Determines if two images A and B greater or equal pixel wise. 
    
    f(a, b) = 1 if a >= b; 0 otherwise.     Parameters
    ----------
    source : Image
    destination : Image
    constant : Number
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.greater_or_equal_constant(source, destination, constant)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greaterOrEqualConstant    

    """


    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'greater_or_equal_constant_' + str(len(dst.shape)) + 'd_x.cl', 'greater_or_equal_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
