from .._tier0 import plugin_function, Image, create_none
import numpy as np

@plugin_function(categories=['label measurement', 'combine', 'map', 'label comparison', 'in assistant'], output_creator=create_none)
def proximal_other_labels_count_map(label_image:Image, other_label_image:Image, count_map:Image = None, maximum_distance: float = 25) -> Image:
    """
    Count number of labels within a given radius in an other label image and returns the result as parametric map.

    Parameters
    ----------
    label_image: Image
    other_label_image: Image
    count_map: Image, optional
        parametric image where the values will be written in.
    maximum_distance: Number, optional
        maximum distance in pixels

    Returns
    -------
    count_map

    """
    from .._tier1 import replace_intensities
    from .._tier3 import proximal_other_labels_count
    # count proximal objects
    count_vector = proximal_other_labels_count(label_image, other_label_image, maximum_distance=maximum_distance)

    # visualize in parametric image
    return replace_intensities(label_image, count_vector, count_map)
