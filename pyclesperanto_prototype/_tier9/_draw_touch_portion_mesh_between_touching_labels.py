from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function

@plugin_function(categories=['label measurement', 'mesh', 'in assistant'])
def draw_touch_portion_mesh_between_touching_labels(labels : Image, touch_portion_mesh_destination : Image = None) -> Image:
    """Starting from a label map, draw lines between touching neighbors 
    resulting in a mesh.
    
    The end points of the lines correspond to the centroids of the labels. The 
    intensity of the lines 
    corresponds to the amount the two labels touch divided by the number of border voxels.
    
    Parameters
    ----------
    labels : Image
    touch_portion_mesh_destination : Image, optional
    
    Returns
    -------
    touch_portion_mesh_destination
    """
    from .._tier9 import centroids_of_labels
    from .._tier4 import generate_touch_portion_matrix
    from .._tier1 import touch_matrix_to_mesh

    centroids = centroids_of_labels(labels)
    touch_portion_matrix = generate_touch_portion_matrix(labels)

    from .._tier1 import set
    set(touch_portion_mesh_destination, 0)

    return touch_matrix_to_mesh(centroids, touch_portion_matrix, touch_portion_mesh_destination)
