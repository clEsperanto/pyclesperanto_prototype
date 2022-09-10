from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def generate_touch_portion_within_range_neighbors_matrix(touch_portion_matrix: Image,
                                                         touch_matrix_destination: Image = None,
                                                         minimum_touch_portion:float=0,
                                                         maximum_touch_portion:float=1.1) -> Image:
    """Generates a touch matrix from a matrix describing how much labels touch
    by selecting the neighbors whose touch portion lies within a specified range.
    Minimum and maximum of that specified range are excluded.

    Parameters
    ----------
    touch_amount_matrix: Image
        can be either a touch-portion or touch-count
    touch_matrix_destination: Image, optional
    minimum_touch_portion: float, optional
    maximum_touch_portion: float, optional

    Returns
    -------
    touch_matrix_destination
    """
    from .._tier1 import binary_and
    return binary_and(touch_portion_matrix > minimum_touch_portion,
               touch_portion_matrix < maximum_touch_portion,
               touch_matrix_destination)
