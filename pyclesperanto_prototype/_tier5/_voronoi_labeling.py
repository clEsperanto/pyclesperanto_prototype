from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_like, create_labels_like
from .._tier4 import connected_components_labeling_box
from .._tier4 import extend_labeling_via_voronoi

@plugin_function(categories=['label', 'in assistant'], output_creator=create_labels_like)
def voronoi_labeling(binary_source : Image, labeling_destination : Image = None):
    """Takes a binary image, labels connected components and dilates the 
    regions using a octagon shape until they touch. 
    
    The resulting label map is written to the output. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.voronoi_labeling(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_voronoiLabeling
    """

    flip = create_like(labeling_destination)

    connected_components_labeling_box(binary_source, flip)

    extend_labeling_via_voronoi(flip, labeling_destination)

    return labeling_destination
