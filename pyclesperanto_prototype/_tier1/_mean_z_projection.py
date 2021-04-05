from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_yx

@plugin_function(output_creator=create_2d_yx, categories=['projection', 'in assistant'])
def mean_z_projection(source : Image, destination : Image = None):
    """Determines the mean average intensity projection of an image along Z. 
    
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
    >>> cle.mean_z_projection(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanZProjection
    """


    parameters = {
        "dst":destination,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/mean_z_projection_x.cl', 'mean_z_projection', destination.shape, parameters)
    return destination
