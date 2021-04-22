from .._tier0 import execute, create_binary_like

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binarize', 'in assistant'], output_creator=create_binary_like)
def greater_or_equal_constant(source : Image, destination : Image = None, constant : float = 0):
    """Determines if two images A and B greater or equal pixel wise. 
    
    f(a, b) = 1 if a >= b; 0 otherwise. 
    
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
    >>> cle.greater_or_equal_constant(source, destination, constant)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greaterOrEqualConstant
    """


    parameters = {
        "src1":source,
        "scalar":float(constant),
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/greater_or_equal_constant_' + str(len(destination.shape)) + 'd_x.cl', 'greater_or_equal_constant_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
