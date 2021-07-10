from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_yx

@plugin_function(output_creator=create_2d_yx, categories=['projection', 'in assistant'])
def standard_deviation_z_projection(source : Image, destination : Image = None):
    """Determines the standard deviation intensity projection of an image 
    stack along Z. 
    
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
    >>> cle.standard_deviation_z_projection(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_standardDeviationZProjection
    """


    parameters = {
        "dst":destination,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/standard_deviation_z_projection_x.cl', 'standard_deviation_z_projection', destination.shape, parameters)
    return destination
