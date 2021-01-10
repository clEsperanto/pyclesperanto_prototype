from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_yz

@plugin_function(output_creator=create_2d_yz, categories=['projection'])
def sum_x_projection(source : Image, destination : Image = None):
    """Determines the sum intensity projection of an image along Z. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.sum_x_projection(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sumXProjection
    """


    parameters = {
        "dst":destination,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/sum_x_projection_x.cl', 'sum_x_projection', destination.shape, parameters)
    return destination
