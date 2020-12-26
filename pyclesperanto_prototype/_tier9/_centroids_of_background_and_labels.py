from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_pointlist_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push

@plugin_function(output_creator=create_pointlist_from_labelmap)
def centroids_of_background_and_labels(source:Image, pointlist_destination :Image = None, regionprops : list = None):
    """todo
    """
    from .._tier9 import centroids_of_labels
    return centroids_of_labels(source, pointlist_destination, True, regionprops)
