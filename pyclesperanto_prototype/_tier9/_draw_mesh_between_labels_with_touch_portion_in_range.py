from .._tier0 import Image, plugin_function

@plugin_function
def draw_mesh_between_labels_with_touch_portion_in_range(labels:Image, mesh_destination:Image=None, minimum_touch_portion:float=0, maximum_touch_portion:float=1.1):
    """Draws a mesh between label centroids where the labels touch portion lies within a given range.
    Minimum and maximum of that specified range are excluded.

    Notes
    -----
    * This operation assumes input images are isotropic.

    Parameters
    ----------
    labels: Image
    mesh_destination: Image, optional
    minimum_touch_portion: float, optional
    maximum_touch_portion: float, optional

    Returns
    -------
    mesh_destination
    """
    from .._tier1 import set_column, set_row, binary_and, touch_matrix_to_mesh
    from .._tier4 import generate_touch_portion_matrix, generate_touch_portion_within_range_neighbors_matrix
    from .._tier9 import centroids_of_labels

    touch_portion_matrix = generate_touch_portion_matrix(labels)
    constrained_matrix = generate_touch_portion_within_range_neighbors_matrix(
                            touch_portion_matrix,
                            minimum_touch_portion=minimum_touch_portion,
                            maximum_touch_portion=maximum_touch_portion
                         )

    # ignore background
    set_column(constrained_matrix, 0, 0)
    set_row(constrained_matrix, 0, 0)

    centroids = centroids_of_labels(labels)

    return touch_matrix_to_mesh(centroids, constrained_matrix, mesh_destination=mesh_destination)
