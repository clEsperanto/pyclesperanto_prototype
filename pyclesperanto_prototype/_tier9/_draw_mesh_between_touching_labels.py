from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function

@plugin_function
def draw_mesh_between_touching_labels(labels : Image, distance_mesh_destination : Image = None):
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_touch_matrix
    from .._tier1 import touch_matrix_to_mesh

    centroids = centroids_of_labels(labels)
    touch_matrix = generate_touch_matrix(labels)
    touch_mesh_destination = touch_matrix_to_mesh(centroids, touch_matrix, distance_mesh_destination)
    return touch_mesh_destination
