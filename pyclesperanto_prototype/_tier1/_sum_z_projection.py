from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_xy

@plugin_function(output_creator=create_2d_xy)
def sum_z_projection(input : Image, output : Image = None):
    """Determines the sum intensity projection of an image along Z.    Parameters
    ----------
    source : Image
    destination_sum : Image
    
    
    Returns
    -------
    destination_sum

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.sum_z_projection(, source, , destination_sum)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sumZProjection    

    """


    parameters = {
        "dst":output,
        "src":input,
    }

    execute(__file__, 'sum_z_projection_x.cl', 'sum_z_projection', output.shape, parameters)
    return output
