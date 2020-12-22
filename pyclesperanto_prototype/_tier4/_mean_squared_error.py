from .._tier0 import create_like
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier3 import squared_difference
from .._tier3 import mean_of_all_pixels

@plugin_function
def mean_squared_error(source1 : Image, source2 : Image):
    """Determines the mean squared error (MSE) between two images. 
    
    The MSE will be stored in a new row of ImageJs
    Results table in the column 'MSE'. 
    
    Parameters
    ----------
    source1 : Image
    source2 : Image
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.mean_squared_error(source1, source2)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanSquaredError
    """
    temp = create_like(source1)

    squared_difference(source1, source2, temp)

    return mean_of_all_pixels(temp)