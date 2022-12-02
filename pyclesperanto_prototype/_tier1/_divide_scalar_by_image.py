from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'])
def divide_scalar_by_image(source : Image, destination : Image = None, scalar : float = 0) -> Image:
    """Divides a scalar by an image pixel by pixel.
    
    <pre>f(x, s) = s / x</pre>
    
    Parameters
    ----------
    source : Image
    destination : Image, optional
    scalar : Number, optional
    
    Returns
    -------
    destination
    """

    parameters = {
        "src":source,
        "dst":destination,
        "scalar":float(scalar)
    }
    execute(__file__, 'divide_scalar_by_image.cl', 'divide_scalar_by_image', destination.shape, parameters)
    return destination
