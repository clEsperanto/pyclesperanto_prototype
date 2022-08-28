from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function

@plugin_function(categories=['label measurement', 'mesh', 'in assistant'])
def draw_touch_portion_mesh_between_touching_labels(labels : Image, touch_portion_mesh_destination : Image = None) -> Image:
    """Starting from a label map, draw lines between touching neighbors resulting in a mesh.
    
    The end points of the lines correspond to the centroids of the labels. The intensity of the lines corresponds
    to the amount the two labels touch divided by the number of border voxels on both labels. Note: label borders at
    image borders are ignored in this calculation.
    
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
    from .._tier1 import touch_matrix_to_mesh, transpose_xy, add_images_weighted

    # as the touch portion is different looking from label A to label B and from label B to label A, we
    # comput the average between those two.
    touch_portion_matrix_A_B = generate_touch_portion_matrix(labels)
    touch_portion_matrix_B_A = transpose_xy(touch_portion_matrix_A_B)

    touch_portion_matrix = add_images_weighted(touch_portion_matrix_A_B, touch_portion_matrix_B_A,
                                               factor1=0.5, factor2=0.5)

    from .._tier1 import set
    set(touch_portion_mesh_destination, 0)

    centroids = centroids_of_labels(labels)
    return touch_matrix_to_mesh(centroids, touch_portion_matrix, touch_portion_mesh_destination)
