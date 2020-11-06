from .._tier0 import execute
from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function
def greater_constant(src1 : Image, dst :Image = None, scalar :float = 0):
    """Determines if two images A and B greater pixel wise. 
    
    f(a, b) = 1 if a > b; 0 otherwise. 

    Parameters
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
    >>> cle.greater_constant(source, destination, constant)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greaterConstant    

    """


    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'greater_constant_' + str(len(dst.shape)) + 'd_x.cl', 'greater_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return dst
