from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import create_like
from pyclesperanto_prototype._tier2 import subtract_images
from pyclesperanto_prototype._tier1 import absolute

@plugin_function
def absolute_difference(source1 : Image, source2 : Image, destination : Image = None):
    """

    Parameters
    ----------
    source1
    source2
    destination

    Returns
    -------

    """

    temp = create_like(destination)

    subtract_images(source1, source2, temp)

    return absolute(temp, destination)