from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def detect_label_edges(label_source :Image, binary_destination :Image = None):
    """Takes a labelmap and returns an image where all pixels on label edges 
    are set to 1 and all other pixels to 0. 
    
    Parameters
    ----------
    label_map : Image
    edge_image_destination : Image
    
    Returns
    -------
    edge_image_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_detectLabelEdges
    """

    parameters = {
        "src_label_map":label_source,
        "dst_edge_image":binary_destination
    }

    execute(__file__, 'detect_label_edges_' + str(len(binary_destination.shape)) + 'd_x.cl', 'detect_label_edges_diamond_' + str(len(binary_destination.shape)) + 'd', binary_destination.shape, parameters)

    return binary_destination
