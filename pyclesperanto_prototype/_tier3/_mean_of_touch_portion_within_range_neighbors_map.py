from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function(categories=['combine', 'neighbor', 'map', 'in assistant'])
def mean_of_touch_portion_within_range_neighbors_map(parametric_map : Image,
                                                     label_map : Image,
                                                     parametric_map_destination : Image = None,
                                                     minimum_touch_portion: float = 0,
                                                     maximum_touch_portion: float = 1.1,
                                                     ignore_touching_background : bool = True) -> Image:
    """Takes a label image and a parametric intensity image and will replace each labels value in the parametric image
    by the mean value of neighboring labels whose touch portion lies within a specified range. The number of most
    touching neighbors can be configured. Minimum and maximum of that specified range are excluded.

    Notes
    -----
    * Values of all pixels in a label each must be identical.
    * This operation assumes input images are isotropic.

    Parameters
    ----------
    parametric_map : Image
    label_map : Image
    parametric_map_destination : Image, optional
    minimum_touch_portion: float, optional
    maximum_touch_portion: float, optional

    Returns
    -------
    parametric_map_destination
    """
    from .._tier1 import read_intensities_from_map, set_column
    from .._tier2 import mean_of_touching_neighbors
    from .._tier1 import replace_intensities
    from .._tier4 import generate_touch_portion_within_range_neighbors_matrix, generate_touch_portion_matrix

    touch_portion_matrix = generate_touch_portion_matrix(label_map)

    # print("n", n)
    touch_matrix = generate_touch_portion_within_range_neighbors_matrix(touch_portion_matrix,
                                                                        minimum_touch_portion=minimum_touch_portion,
                                                                        maximum_touch_portion=maximum_touch_portion)
    # print("TM", touch_matrix)

    if ignore_touching_background:
        set_column(touch_matrix, 0)

    intensities = read_intensities_from_map(label_map, parametric_map)
    # print("in in", intensities)

    new_intensities = mean_of_touching_neighbors(intensities, touch_matrix)
    # print("in out", new_intensities)

    parametric_map_destination = replace_intensities(label_map, new_intensities, parametric_map_destination)

    return parametric_map_destination
