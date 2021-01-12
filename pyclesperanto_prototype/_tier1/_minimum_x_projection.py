from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_yz

@plugin_function(output_creator=create_2d_yz, categories=['projection'])
def minimum_x_projection(source : Image, destination_min : Image = None):
    """Determines the minimum intensity projection of an image along Y. 
    
    Parameters
    ----------
    source : Image
    destination_min : Image
    
    Returns
    -------
    destination_min
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.minimum_x_projection(source, destination_min)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumXProjection
    """


    parameters = {
        "dst_min":destination_min,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/minimum_x_projection_x.cl', 'minimum_x_projection', destination_min.shape, parameters)
    return destination_min
