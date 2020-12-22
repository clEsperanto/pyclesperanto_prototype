from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier9 import centroids_of_labels
from .._tier1 import generate_distance_matrix
from .._tier1 import set_where_x_equals_y
from .._tier1 import set_row
from .._tier1 import set_column
from .._tier1 import set
from .._tier1 import point_index_list_to_mesh
from .._tier1 import n_closest_points

@plugin_function(categories=['label measurement', 'mesh', 'in assistant'])
def draw_mesh_between_proximal_labels(labels : Image, mesh_target : Image = None, maximum_distance : int = 1):
    """Starting from a label map, draw lines between labels that are closer 
    than a given distance resulting in a mesh.
    
    The end points of the lines correspond to the centroids of the labels. 
    
    Parameters
    ----------
    input : Image
    destination : Image
    maximum_distance : Number
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_drawMeshBetweenProximalLabels
    """
    pointlist = centroids_of_labels(labels)

    distance_matrix = generate_distance_matrix(pointlist, pointlist)

    from .._tier2 import distance_matrix_to_mesh

    from .._tier1 import set
    set(mesh_target, 0)

    mesh_target = distance_matrix_to_mesh(pointlist, distance_matrix, mesh_target, maximum_distance)
    return mesh_target
