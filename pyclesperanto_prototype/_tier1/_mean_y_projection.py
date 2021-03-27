from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_zx

@plugin_function(output_creator=create_2d_zx, categories=['projection'])
def mean_y_projection(source : Image, destination : Image = None):
    """Determines the mean average intensity projection of an image along Y. 
    
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
    >>> cle.mean_y_projection(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanYProjection
    """


    parameters = {
        "dst":destination,
        "src":source,
    }

    execute(__file__, '../clij-opencl-kernels/kernels/mean_y_projection_x.cl', 'mean_y_projection', destination.shape, parameters)
    return destination
