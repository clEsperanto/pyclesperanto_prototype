from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np
from .._tier0 import create_none


@plugin_function(categories=['label measurement'], output_creator=create_none)
def touch_portion_within_range_neighbor_count(labels: Image,
                                              count_vector_destination: Image = None,
                                              minimum_touch_portion: float = 0,
                                              maximum_touch_portion: float = 1.1) -> Image:
    """Takes a label map, determines which labels are touch within a given portion range
    and returns the number of those in a vector.

    Notes
    -----
    * This operation assumes input images are isotropic.

    Parameters
    ----------
    labels : Image
    count_vector_destination : Image, optional
    minimum_touch_portion : float, optional
    maximum_touch_portion : float, optional

    Returns
    -------
    destination
    """
    from .._tier1 import set_column, set_row
    from .._tier4 import generate_touch_portion_within_range_neighbors_matrix, generate_touch_portion_matrix
    from .._tier1 import count_touching_neighbors

    touch_portion_matrix = generate_touch_portion_matrix(labels)

    # ignore touching background
    set_row(touch_portion_matrix, 0, 0)
    set_column(touch_portion_matrix, 0, 0)

    touch_matrix = generate_touch_portion_within_range_neighbors_matrix(touch_portion_matrix,
                                                                        minimum_touch_portion=minimum_touch_portion,
                                                                        maximum_touch_portion=maximum_touch_portion)
    count_vector_destination = count_touching_neighbors(touch_matrix, count_vector_destination)
    set_column(count_vector_destination, 0, 0)
    return count_vector_destination
