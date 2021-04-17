from .._tier0 import execute, create_binary_like

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'binarize', 'in assistant'], output_creator=create_binary_like)
def greater(source1 : Image, source2 : Image, destination : Image = None):
    """Determines if two images A and B greater pixel wise.
    
    f(a, b) = 1 if a > b; 0 otherwise. 
    
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
    >>> cle.greater(source1, source2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greater
    """


    parameters = {
        "src1":source1,
        "src2":source2,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/greater_' + str(len(destination.shape)) + 'd_x.cl', 'greater_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
