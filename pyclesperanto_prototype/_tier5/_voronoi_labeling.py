from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_like
from .._tier4 import connected_components_labeling_box
from .._tier4 import extend_labeling_via_voronoi

@plugin_function
def voronoi_labeling(binary_source : Image, labeling_destination : Image = None):
    """

    Returns
    -------

    """

    flip = create_like(labeling_destination)

    connected_components_labeling_box(binary_source, flip)

    extend_labeling_via_voronoi(flip, labeling_destination)

    return labeling_destination
