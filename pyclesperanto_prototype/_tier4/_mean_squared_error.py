from .._tier0 import create_like
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier3 import squared_difference
from .._tier3 import mean_of_all_pixels

@plugin_function
def mean_squared_error(source1 : Image, source2 : Image):
    """

    Parameters
    ----------
    source1
    source2

    Returns
    -------

    """
    temp = create_like(source1)

    squared_difference(source1, source2, temp)

    return mean_of_all_pixels(temp)