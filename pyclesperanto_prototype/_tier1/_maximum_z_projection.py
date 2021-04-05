from .._tier0 import execute
from .._tier0 import create_2d_yx
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_2d_yx, categories=['projection', 'in assistant'])
def maximum_z_projection(source :Image, destination_max :Image = None):
    """Determines the maximum intensity projection of an image along Z. 
    
    Parameters
    ----------
    source : Image
    destination_max : Image
    
    Returns
    -------
    destination_max
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.maximum_z_projection(source, destination_max)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumZProjection
    """


    parameters = {
        "dst_max":destination_max,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/maximum_z_projection_x.cl', 'maximum_z_projection', destination_max.shape, parameters)

    return destination_max
