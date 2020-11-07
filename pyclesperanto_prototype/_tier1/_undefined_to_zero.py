from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def undefined_to_zero(source : Image, destination : Image = None):
    """

    """


    parameters = {
        "dst":destination,
        "src":source
    }

    execute(__file__, 'undefined_to_zero_x.cl', 'undefined_to_zero', destination.shape, parameters)
    return destination
