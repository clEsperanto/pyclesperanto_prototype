from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier9 import centroids_of_labels
from .._tier1 import generate_distance_matrix
from .._tier1 import set_where_x_equals_y
from .._tier1 import set_row
from .._tier1 import set_column
from .._tier1 import set
from .._tier1 import pointindexlist_to_mesh
from .._tier1 import n_closest_points

@plugin_function
def draw_mesh_between_proximal_labels(labels : Image, mesh_target : Image = None, maximum_distance : int = 1):
    """

    Parameters
    ----------
    labels
    mesh_target
    maximum_distance

    Returns
    -------

    """
    pointlist = centroids_of_labels(labels)

    distance_matrix = generate_distance_matrix(pointlist, pointlist)

    from .._tier2 import distance_matrix_to_mesh

    from .._tier1 import set
    set(mesh_target, 0)

    mesh_target = distance_matrix_to_mesh(pointlist, distance_matrix, mesh_target, maximum_distance)
    return mesh_target
