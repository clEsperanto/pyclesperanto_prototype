from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function
def draw_mesh_between_n_most_touching_labels(labels: Image, mesh_destination: Image = None, n: int = 1) -> Image:
    """Draws a mesh between most touching neighbors

    Notes
    -----
    * This operation assumes input images are isotropic.

    Parameters
    ----------
    labels: Image
    mesh_destination:Image, optional
    n: int
    """
    from .._tier1 import touch_matrix_to_mesh, set
    from .._tier3 import generate_touch_count_matrix
    from .._tier4 import generate_n_most_touching_neighbors_matrix
    from .._tier9 import centroids_of_labels

    centroids = centroids_of_labels(labels)
    # print("centroids shape", centroids.shape)

    touch_count_matrix = generate_touch_count_matrix(labels)
    # print("TCM:\n", touch_count_matrix)
    touch_matrix = generate_n_most_touching_neighbors_matrix(touch_count_matrix, n=n)
    # print("TM shape", touch_matrix.shape)
    # print("TM:\n", touch_matrix)
    set(mesh_destination, 0)
    mesh_destination = touch_matrix_to_mesh(centroids, touch_matrix, mesh_destination)
    return mesh_destination

