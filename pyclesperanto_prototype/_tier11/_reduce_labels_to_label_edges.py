from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_labels_like

@plugin_function(categories=['label processing', 'in assistant', 'bia-bob-suggestion'], output_creator=create_labels_like)
def reduce_labels_to_label_edges(source:Image, destination:Image=None) -> Image:
    """Takes a label map and reduces all labels to their edges. Label IDs stay and background will be zero.

    Parameters
    ----------
    source: Image
    destination: Image, optional

    Returns
    -------
    destination

    See Also
    --------
    ..[0] https://clij.github.io/clij2-docs/reference_reduceLabelsToLabelEdges
    """
    from .._tier1 import mask, detect_label_edges

    binary = detect_label_edges(source)
    mask(source, binary, destination)

    return destination