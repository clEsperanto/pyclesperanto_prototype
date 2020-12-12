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
def draw_mesh_between_n_closest_labels(labels : Image, mesh_target : Image = None, n : int = 1):
    pointlist = centroids_of_labels(labels)

    distance_matrix = generate_distance_matrix(pointlist, pointlist)

    import numpy as np
    max_float = np.finfo(np.float).max

    set_where_x_equals_y(distance_matrix, max_float)
    set_row(distance_matrix, 0, max_float)
    set_column(distance_matrix, 0, max_float)

    set(mesh_target, 0)
    indexlist = n_closest_points(distance_matrix, n=n)
    pointindexlist_to_mesh(pointlist, indexlist, mesh_target)

    return mesh_target
