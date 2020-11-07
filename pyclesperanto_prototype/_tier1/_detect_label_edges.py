from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def detect_label_edges(label_source :Image, binary_destination :Image = None):
    """
    blad
    """

    parameters = {
        "src_label_map":label_source,
        "dst_edge_image":binary_destination
    }

    execute(__file__, 'detect_label_edges_' + str(len(binary_destination.shape)) + 'd_x.cl', 'detect_label_edges_diamond_' + str(len(binary_destination.shape)) + 'd', binary_destination.shape, parameters)

    return binary_destination
