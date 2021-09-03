from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function

@plugin_function(categories=['label measurement', 'mesh'])
def draw_angle_mesh_between_touching_labels(labels : Image, angle_mesh_destination : Image = None):
    """Starting from a label map, draw lines between touching neighbors 
    resulting in a mesh.
    
    The end points of the lines correspond to the centroids of the labels. The 
    intensity of the lines 
    corresponds to the angle in degrees between these labels (in pixels or voxels).
    
    Parameters
    ----------
    labels : Image
    angle_mesh_destination : Image
    
    Returns
    -------
    angle_mesh_destination
    
    References
    ----------
    """
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_angle_matrix
    from .._tier1 import generate_touch_matrix
    from .._tier1 import touch_matrix_to_mesh
    from .._tier1 import multiply_images
    from .._tier2 import radians_to_degrees

    centroids = centroids_of_labels(labels)
    angle_matrix = generate_angle_matrix(centroids, centroids)
    touch_matrix = generate_touch_matrix(labels)
    touch_angle_matrix = multiply_images(touch_matrix, angle_matrix)
    touch_angle_matrix = radians_to_degrees(touch_angle_matrix)

    from .._tier1 import set
    set(angle_mesh_destination, 0)

    angle_mesh_destination = touch_matrix_to_mesh(centroids, touch_angle_matrix, angle_mesh_destination)
    return angle_mesh_destination
