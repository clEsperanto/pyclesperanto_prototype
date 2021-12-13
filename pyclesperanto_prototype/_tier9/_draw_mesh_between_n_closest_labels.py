from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier9 import centroids_of_labels
from .._tier1 import generate_distance_matrix
from .._tier1 import set_where_x_equals_y
from .._tier1 import set_row
from .._tier1 import set_column
from .._tier1 import point_index_list_to_mesh
from .._tier1 import n_closest_points

@plugin_function(categories=['label measurement', 'mesh', 'in assistant'])
def draw_mesh_between_n_closest_labels(labels : Image, mesh_target : Image = None, n : int = 1):
    """Starting from a label map, draw lines between n closest labels for each 
    label resulting in a mesh.
    
    The end points of the lines correspond to the centroids of the labels. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    number_of_closest_labels : Number
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_drawMeshBetweenNClosestLabels
    """
    pointlist = centroids_of_labels(labels)

    distance_matrix = generate_distance_matrix(pointlist, pointlist)

    import numpy as np
    max_float = np.finfo(float).max

    set_where_x_equals_y(distance_matrix, max_float)
    set_row(distance_matrix, 0, max_float)
    set_column(distance_matrix, 0, max_float)

    from .._tier1 import set
    set(mesh_target, 0)
    indexlist = n_closest_points(distance_matrix, n=n)
    point_index_list_to_mesh(pointlist, indexlist, mesh_target)

    return mesh_target
