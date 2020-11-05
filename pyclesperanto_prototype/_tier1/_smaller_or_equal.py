from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def smaller_or_equal(src1 : Image, src2 : Image, dst : Image = None):
    """Determines if two images A and B smaller or equal pixel wise.
    
    f(a, b) = 1 if a <= b; 0 otherwise.     Parameters
    ----------
    source1 : Image
    source2 : Image
    destination : Image
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.smaller_or_equal(, source1, , source2, , destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_smallerOrEqual    

    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'smaller_or_equal_' + str(len(dst.shape)) + 'd_x.cl', 'smaller_or_equal_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
