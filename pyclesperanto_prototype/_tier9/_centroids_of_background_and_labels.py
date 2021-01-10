from .._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_none)
def centroids_of_background_and_labels(source:Image, pointlist_destination :Image = None):
    """See centroids_of_labels
    """
    from .._tier9 import centroids_of_labels
    return centroids_of_labels(source, pointlist_destination, True)
