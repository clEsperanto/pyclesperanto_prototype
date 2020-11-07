from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier1 import multiply_image_and_scalar

@plugin_function
def invert(source : Image, destination :Image = None):
    """
    bla
    """

    multiply_image_and_scalar(source, destination, -1)

    return destination
