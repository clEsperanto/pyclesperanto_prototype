import numpy as np

import pyclesperanto_prototype
from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def statistics_of_labelled_neighbors(label_image: Image,
                                     proximal_distances = (10, 20, 40, 80, 160),
                                     nearest_neighbor_ns = (1, 2, 3, 4, 5, 6, 7, 8, 10, 20)):
    """Determine statistics of labeled objects such as average/min/mas neighbor distances, number of neighbors in a
    given radius, touch portion etc.

    Parameters
    ----------
    label_image: Image
    proximal_distances: list of float, optional
        will determine statistics for neighbors within specified distances
    nearest_neighbor_ns: list of int, optional
        will determine statistics of specified n nearest neighbors

    Returns
    -------
    pandas.DataFrame
    """
    import pandas as pd

    from .._tier1 import generate_distance_matrix, generate_touch_matrix, replace_intensity, sum_y_projection
    from .._tier1 import minimum_distance_of_touching_neighbors, average_distance_of_touching_neighbors, maximum_distance_of_touching_neighbors
    from .._tier1 import average_distance_of_n_nearest_distances, maximum_distance_of_n_shortest_distances
    from .._tier1 import count_touching_neighbors, average_distance_of_n_far_off_distances
    from .._tier1 import maximum_y_projection, minimum_y_projection, copy, set_where_x_equals_y, nan_to_num

    from .._tier3 import generate_proximal_neighbors_matrix
    from .._tier3 import generate_touch_count_matrix
    from .._tier4 import generate_touch_portion_matrix
    from .._tier9 import centroids_of_labels
    from .._tier11 import standard_deviation_touch_portion

    #print("num labels", label_image.max())
    all_stats = {"label": np.arange(1, label_image.max() + 1).astype(int)}

    centroids = centroids_of_labels(label_image)
    #print("centroids:", centroids.shape)

    distance_matrix = generate_distance_matrix(centroids, centroids)
    #print("distance matrix", distance_matrix.shape)

    touch_matrix = generate_touch_matrix(label_image)
    #print("touch matrix", touch_matrix.shape)

    all_stats["touching_neighbor_count"] = cle_to_numpy(remove_first=True,
                                                                       data=count_touching_neighbors(touch_matrix))

    # distances of touching neighbors
    all_stats["minimum_distance_of_touching_neighbors"] = cle_to_numpy(remove_first=True,
                                                                       data=minimum_distance_of_touching_neighbors(
                                                                           distance_matrix, touch_matrix))
    all_stats["average_distance_of_touching_neighbors"] = cle_to_numpy(remove_first=True,
                                                                       data=average_distance_of_touching_neighbors(
                                                                           distance_matrix, touch_matrix))
    all_stats["maximum_distance_of_touching_neighbors"] = cle_to_numpy(remove_first=True,
                                                                       data=maximum_distance_of_touching_neighbors(
                                                                           distance_matrix, touch_matrix))

    # number of neighbors within given radii
    for d in proximal_distances:
        proximal_touch_matrix = generate_proximal_neighbors_matrix(distance_matrix,
                                                              min_distance=0,
                                                              max_distance=d)

        all_stats["proximal_neighbor_count_d" + str(d)] = cle_to_numpy(remove_first=True,
                                                                       data=count_touching_neighbors(proximal_touch_matrix))

    # for determining nearest neighbors, we need to set distance-to-self to a
    # large number so that we do not find ourselves
    self_far_distance_matrix = copy(distance_matrix)
    set_where_x_equals_y(self_far_distance_matrix, distance_matrix.max() + 1)

    # distances of n-nearest neighbors
    for n in nearest_neighbor_ns:
        # max distance
        all_stats["maximum_distance_of_n" + str(n) + "_nearest_neighbors"] = \
            cle_to_numpy(remove_first=True,
                         data=maximum_distance_of_n_shortest_distances(self_far_distance_matrix, n=n))

        # mean distance
        all_stats["average_distance_of_n" + str(n) + "_nearest_neighbors"] = \
            cle_to_numpy(remove_first=True,
                         data=average_distance_of_n_nearest_distances(self_far_distance_matrix, n=n))

    all_stats["distance_to_most_distant_other"] = \
        cle_to_numpy(remove_first=True, data=average_distance_of_n_far_off_distances(distance_matrix, n=1))

    # touch count / portion
    touch_count_matrix = generate_touch_count_matrix(label_image)
    touch_portion_matrix = generate_touch_portion_matrix(label_image)

    # To detect the minimum touch count/portion, we need to set all 0 pixels to a high value
    touch_count_matrix_0_set_to_high = replace_intensity(touch_count_matrix,
                                                             value_to_replace=0,
                                                             value_replacement=touch_count_matrix.max())

    temp = nan_to_num(touch_portion_matrix)
    touch_portion_matrix_0_set_to_high = replace_intensity(
        temp,
        value_to_replace=0,
        value_replacement=temp.max())

    # number of pixels where the label touches others; excluding image borders
    all_stats["touch_count_sum"] = cle_to_numpy(remove_first=True, data=sum_y_projection(touch_count_matrix))
    all_stats["minimum_touch_count"] = cle_to_numpy(remove_first=True,
                                                   data=minimum_y_projection(touch_count_matrix_0_set_to_high))
    all_stats["maximum_touch_count"] = cle_to_numpy(remove_first=True,
                                                    data=maximum_y_projection(touch_count_matrix))

    all_stats["minimum_touch_portion"] = cle_to_numpy(remove_first=True,
                                                     data=minimum_y_projection(touch_portion_matrix_0_set_to_high))
    all_stats["maximum_touch_portion"] = cle_to_numpy(remove_first=True,
                                                      data=maximum_y_projection(touch_portion_matrix))

    # todo: this might be possible more efficiently by refactoring; at the moment it takes the label image
    all_stats["standard_deviation_touch_portion"] = cle_to_numpy(remove_first=True,
                                                                 data=standard_deviation_touch_portion(label_image))

    return pd.DataFrame(all_stats)


def cle_to_numpy(data, remove_first=False):
    result = np.asarray(data)
    if len(result.shape) == 2:
        result = result[0]
    if remove_first:
        result = result[1:]
    return result
