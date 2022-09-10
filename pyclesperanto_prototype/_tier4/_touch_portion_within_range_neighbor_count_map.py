from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np


@plugin_function(categories=['label measurement', 'map', 'in assistant'])
def touch_portion_within_range_neighbor_count_map(labels: Image,
                                                  map_destination: Image = None,
                                                  minimum_touch_portion: float = 0,
                                                  maximum_touch_portion: float = 1.1) -> Image:
    """Takes a label map, determines which labels are touching within a given portion range
    and replaces every label with the number of neighboring labels.

    Parameters
    ----------
    labels : Image
    map_destination : Image, optional
    minimum_touch_portion : float, optional
    maximum_touch_portion : float, optional

    Returns
    -------
    destination
    """
    from ._touch_portion_within_range_neighbor_count import touch_portion_within_range_neighbor_count
    from .._tier1 import replace_intensities

    number_of_touching_neighbors_vector = touch_portion_within_range_neighbor_count(labels, minimum_touch_portion=minimum_touch_portion,
                                                                  maximum_touch_portion=maximum_touch_portion)

    replace_intensities(labels, number_of_touching_neighbors_vector, map_destination)
    return map_destination
