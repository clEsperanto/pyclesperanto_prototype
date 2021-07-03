from .._tier4 import connected_components_labeling_box
from .._tier1 import nonzero_minimum_diamond

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_labels_like

@plugin_function(categories=['label', 'in assistant'], output_creator=create_labels_like)
def connected_components_labeling_diamond(binary_input: Image, labeling_destination: Image = None):
    """Performs connected components analysis inspecting the diamond 
    neighborhood of every pixel to a binary image and generates a label 
    map. 
    
    Parameters
    ----------
    binary_input : Image
    labeling_destination : Image
    
    Returns
    -------
    labeling_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.connected_components_labeling_diamond(binary_input, labeling_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_connectedComponentsLabelingDiamond
    """
    connected_components_labeling_box(binary_input, labeling_destination, nonzero_minimum_diamond)

    return labeling_destination
