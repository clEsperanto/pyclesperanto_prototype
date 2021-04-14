from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_yx

@plugin_function(output_creator=create_2d_yx, categories=['projection', 'in assistant'])
def minimum_z_projection(source : Image, destination_min : Image = None):
    """Determines the minimum intensity projection of an image along Z. 
    
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
    >>> cle.minimum_z_projection(source, destination_min)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumZProjection
    """


    parameters = {
        "dst_min":destination_min,
        "src":source,
    };

    execute(__file__, '../clij-opencl-kernels/kernels/minimum_z_projection_x.cl', 'minimum_z_projection', destination_min.shape, parameters);
    return destination_min
