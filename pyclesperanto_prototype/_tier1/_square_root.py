from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'], priority=-1)
def square_root(source : Image, destination : Image = None) -> Image:
    """Computes the square root of each pixel.

    Parameters
    ----------
    source : Image
    destination : Image, optional

    Returns
    -------
    destination
    
    Examples
    --------
    """

    parameters = {
        "dst": destination,
        "src":source,
    }

    execute(__file__, 'square_root.cl', 'square_root', destination.shape, parameters)

    return destination
