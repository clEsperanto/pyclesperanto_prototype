from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function

@plugin_function(categories=['label measurement', 'mesh', 'in assistant'])
def draw_distance_mesh_between_proximal_labels(labels: Image, distance_mesh_destination: Image = None, maximum_distance: float = 1) -> Image:
    """Starting from a label map, draw lines between neighbors that a closer than a
    defined upper bound resulting in a mesh.
    
    The end points of the lines correspond to the centroids of the labels. The 
    intensity of the lines 
    corresponds to the distance between these labels (in pixels or voxels). 

    Notes
    -----
    * This operation assumes input images are isotropic.

    Parameters
    ----------
    labels : Image
    distance_mesh_destination : Image, optional
    maximum_distance : float, optional
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_drawDistanceMeshBetweenTouchingLabels
    """
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier3 import generate_proximal_neighbors_matrix
    from .._tier1 import touch_matrix_to_mesh
    from .._tier1 import multiply_images
    from .._tier1 import set

    centroids = centroids_of_labels(labels)
    distance_matrix = generate_distance_matrix(centroids, centroids)
    proximal_neighbor_matrix = generate_proximal_neighbors_matrix(distance_matrix, max_distance=maximum_distance)

    touch_distance_matrix = multiply_images(proximal_neighbor_matrix, distance_matrix)

    # remove links to centroid of background
    set(distance_mesh_destination, 0)

    distance_mesh_destination = touch_matrix_to_mesh(centroids, touch_distance_matrix, distance_mesh_destination)
    return distance_mesh_destination
