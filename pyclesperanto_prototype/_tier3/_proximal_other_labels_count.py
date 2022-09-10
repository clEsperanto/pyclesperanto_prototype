from .._tier0 import plugin_function, Image, create_none
import numpy as np

@plugin_function(categories=['label measurement', 'combine', 'map', 'label comparison'], output_creator=create_none)
def proximal_other_labels_count(label_image:Image, other_label_image:Image, count_vector:Image = None, maximum_distance:float = 25) -> Image:
    """
    Count number of labels within a given radius in an other label image and returns the result as vector.

    Notes
    -----
    * This operation assumes input images are isotropic.

    Parameters
    ----------
    label_image: Image
    other_label_image: Image
    count_vector: Image, optional
        vector (num_labels + 1 long) where the values will be written in. The first column (index 0, value 0)
        corresponds to background.
    maximum_distance: Number, optional
        maximum distance in pixels

    Returns
    -------
    count_vector

    """
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix, set_row, set_column, smaller_or_equal_constant, sum_y_projection
    centroids_a = centroids_of_labels(label_image)
    centroids_b = centroids_of_labels(other_label_image)

    distance_matrix = generate_distance_matrix(centroids_a, centroids_b)

    # ignore distance to background
    set_row(distance_matrix, 0, np.finfo(np.float32).max)
    set_column(distance_matrix, 0, np.finfo(np.float32).max)

    # threshold matrix
    binary_matrix = smaller_or_equal_constant(distance_matrix, constant=maximum_distance)

    # count objects in each column of that matrix
    count_vector = sum_y_projection(binary_matrix, count_vector)

    return count_vector