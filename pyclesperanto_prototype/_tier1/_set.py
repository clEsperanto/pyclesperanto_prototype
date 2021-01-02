from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set(source : Image, scalar : float = 0):
    """Sets all pixel values x of a given image X to a constant value v.
    
    <pre>f(x) = v</pre> 
    
    Parameters
    ----------
    source : Image
    value : Number
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.set(source, value)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_set
    """


    parameters = {
        "dst":source,
        "value":float(scalar)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/set_' + str(len(source.shape)) + 'd_x.cl', 'set_' + str(len(source.shape)) + 'd', source.shape, parameters);
    return source
