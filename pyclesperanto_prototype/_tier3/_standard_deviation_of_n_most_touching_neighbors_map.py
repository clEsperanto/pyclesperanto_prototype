from .._tier0 import Image, plugin_function

@plugin_function(categories=['combine', 'neighbor', 'map', 'in assistant'])
def standard_deviation_of_n_most_touching_neighbors_map(parametric_map: Image, label_map: Image,
                                                        parametric_map_destination: Image = None, n: int = 1,
                                                        ignore_touching_background: bool = True) -> Image:
    """Takes a label image and a parametric intensity image and will replace each labels value in the parametric image
    by the standard_deviation value of most touching neighboring labels. The number of most touching neighbors can be configured.
    Note: Values of all pixels in a label each must be identical.

    Parameters
    ----------
    parametric_map : Image
    label_map : Image
    parametric_map_destination : Image, optional
    n : int
        number of most touching neighbors

    Returns
    -------
    parametric_map_destination
    """
    from .._tier1 import read_intensities_from_map, set_column
    from .._tier2 import standard_deviation_of_touching_neighbors
    from .._tier1 import replace_intensities
    from .._tier3 import generate_touch_count_matrix
    from .._tier4 import generate_n_most_touching_neighbors_matrix

    touch_count_matrix = generate_touch_count_matrix(label_map)

    touch_matrix = generate_n_most_touching_neighbors_matrix(touch_count_matrix, n=n)

    if ignore_touching_background:
        set_column(touch_matrix, 0)

    intensities = read_intensities_from_map(label_map, parametric_map)

    new_intensities = standard_deviation_of_touching_neighbors(intensities, touch_matrix)

    parametric_map_destination = replace_intensities(label_map, new_intensities, parametric_map_destination)

    return parametric_map_destination
