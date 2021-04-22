from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'binarize', 'in assistant'])
def smaller_or_equal(source1 : Image, source2 : Image, destination : Image = None, output_creator=create_binary_like):
    """Determines if two images A and B smaller or equal pixel wise.
    
    f(a, b) = 1 if a <= b; 0 otherwise. 
    
    Parameters
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
    >>> cle.smaller_or_equal(source1, source2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_smallerOrEqual
    """


    parameters = {
        "src1":source1,
        "src2":source2,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/smaller_or_equal_' + str(len(destination.shape)) + 'd_x.cl', 'smaller_or_equal_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
