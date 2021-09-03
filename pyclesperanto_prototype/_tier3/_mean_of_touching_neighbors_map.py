from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'neighbor', 'map', 'in assistant'])
def mean_of_touching_neighbors_map(parametric_map : Image, label_map : Image, parametric_map_destination : Image = None, radius : int = 1, ignore_touching_background : bool = True):
    """Takes a label image and a parametric intensity image and will replace each labels value in the parametric image
    by the mean value of neighboring labels. The radius of the neighborhood can be configured:
    * radius 0: Nothing is replaced
    * radius 1: direct neighbors are averaged
    * radius 2: neighbors and neighbors or neighbors are averaged
    * radius n: ...

    Note: Values of all pixels in a label each must be identical.

    Parameters
    ----------
    parametric_map : Image
    label_map : Image
    parametric_map_destination : Image
    radius : int
    ignore_touching_background : bool

    Returns
    -------
    parametric_map_destination

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanOfTouchingNeighbors
    """
    from .._tier1 import copy
    from .._tier1 import generate_touch_matrix
    from .._tier2 import neighbors_of_neighbors
    from .._tier1 import read_intensities_from_map
    from .._tier2 import mean_of_touching_neighbors
    from .._tier1 import replace_intensities
    from .._tier1 import set_column

    if radius == 0:
        return copy(parametric_map, parametric_map_destination)

    touch_matrix = generate_touch_matrix(label_map)
    if ignore_touching_background:
        set_column(touch_matrix, 0)

    for i in range(1, int(radius)):
        touch_matrix = neighbors_of_neighbors(touch_matrix)
        if ignore_touching_background:
            set_column(touch_matrix, 0)

    intensities = read_intensities_from_map(label_map, parametric_map)

    new_intensities = mean_of_touching_neighbors(intensities, touch_matrix)

    set_column(new_intensities, 0, 0)

    parametric_map_destination = replace_intensities(label_map, new_intensities, parametric_map_destination)

    return parametric_map_destination
