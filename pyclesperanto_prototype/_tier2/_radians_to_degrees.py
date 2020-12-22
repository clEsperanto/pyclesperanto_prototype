from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import multiply_image_and_scalar

@plugin_function
def radians_to_degrees(source : Image, destination : Image = None):
    """Converts radians to degrees
    """
    import numpy as np
    return multiply_image_and_scalar(source, destination, 180.0 / np.pi)
