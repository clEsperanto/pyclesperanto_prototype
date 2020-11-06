from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_xy

@plugin_function(output_creator=create_2d_xy)
def mean_z_projection(input : Image, output : Image):
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
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanZProjection    

    """


    parameters = {
        "dst":output,
        "src":input,
    }

    execute(__file__, 'mean_z_projection_x.cl', 'mean_z_projection', output.shape, parameters)
    return output
