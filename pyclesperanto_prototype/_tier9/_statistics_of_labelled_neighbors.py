import numpy as np

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def statistics_of_labelled_neighbors(label_image: Image,
                                     proximal_distances = (10, 20, 40, 80, 160),
                                     nearest_neighbor_ns = (1, 2, 3, 4, 5, 6, 7, 8, 10, 20),
                                     dilation_radii = (5, 10)):
    """Determine statistics of labeled objects such as average/min/mas neighbor distances, number of neighbors in a
    given radius, touch portion etc.

    Notes
    -----
    * This operation assumes input images are isotropic.

    Parameters
    ----------
    label_image: Image
    proximal_distances: list of float, optional
        will determine statistics for neighbors within specified distances
    nearest_neighbor_ns: list of int, optional
        will determine statistics of specified n nearest neighbors
    dilation_radii: list of int, optional
        will determine statistics of touching neighbors after dilating the labels with given radii

    Returns
    -------
    pandas.DataFrame
    """
    from .._tier1 import generate_distance_matrix, generate_touch_matrix, replace_intensity, sum_y_projection
    from .._tier1 import minimum_distance_of_touching_neighbors, average_distance_of_touching_neighbors, maximum_distance_of_touching_neighbors
    from .._tier1 import average_distance_of_n_nearest_distances, maximum_distance_of_n_shortest_distances
    from .._tier1 import count_touching_neighbors, average_distance_of_n_far_off_distances, set_column, set_row
    from .._tier1 import maximum_y_projection, minimum_y_projection, copy, set_where_x_equals_y, nan_to_num

    from .._tier3 import generate_proximal_neighbors_matrix
    from .._tier3 import generate_touch_count_matrix
    from .._tier4 import generate_touch_portion_matrix, generate_touch_portion_within_range_neighbors_matrix
    from .._tier9 import centroids_of_labels
    from .._tier11 import standard_deviation_touch_portion
    from .._tier4 import dilate_labels

    #print("num labels", label_image.max())
    all_stats = {"label": np.arange(1, label_image.max() + 1).astype(int)}

    centroids = centroids_of_labels(label_image)
    #print("centroids:", centroids.shape)

    distance_matrix = generate_distance_matrix(centroids, centroids)
    #print("distance matrix", distance_matrix.shape)

    touch_matrix = generate_touch_matrix(label_image)
    # ignore touching background
    set_column(touch_matrix, 0, 0)
    set_row(touch_matrix, 0, 0)

    #print("touch matrix", touch_matrix)

    all_stats["touching_neighbor_count"] = cle_to_numpy(remove_first=True,
                                                                       data=count_touching_neighbors(touch_matrix))

    #print("tnc", all_stats["touching_neighbor_count"])

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

    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        all_stats["max_min_distance_ratio_of_touching_neighbors"] = all_stats["maximum_distance_of_touching_neighbors"] / all_stats["minimum_distance_of_touching_neighbors"]

    #print("distance_matrix", distance_matrix)

    # number of neighbors within given radii
    for d in proximal_distances:
        proximal_touch_matrix = generate_proximal_neighbors_matrix(distance_matrix,
                                                              min_distance=0,
                                                              max_distance=d)
        #print("proximal_touch_matrix", d,"\n", proximal_touch_matrix)

        all_stats["proximal_neighbor_count_d" + str(d)] = cle_to_numpy(remove_first=True,
                                                                       data=count_touching_neighbors(proximal_touch_matrix))
        #print("count", all_stats["proximal_neighbor_count_d" + str(d)])

    #print("----------------------")

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
    # ignore touching background
    set_column(touch_count_matrix, 0, 0)
    set_row(touch_count_matrix, 0, 0)
    set_column(touch_portion_matrix, 0, 0)
    set_row(touch_portion_matrix, 0, 0)

    # To detect the minimum touch count/portion, we need to set all 0 pixels to a high value
    touch_count_matrix_0_set_to_high = replace_intensity(touch_count_matrix,
                                                             value_to_replace=0,
                                                             value_replacement=touch_count_matrix.max())

    #print("touch_portion_matrix", touch_portion_matrix)

    for touch_portion_threshold in [0, 0.16, 0.2, 0.33, 0.5, 0.75]:
        touch_portion_within_range_neighbors_matrix = generate_touch_portion_within_range_neighbors_matrix(touch_portion_matrix,
                                                             minimum_touch_portion=touch_portion_threshold)

        #print("> ", touch_portion_threshold, touch_portion_within_range_neighbors_matrix)

        all_stats["touch_portion_above_" + str(touch_portion_threshold) + "_neighbor_count"] = cle_to_numpy(remove_first=True,
                                                                       data=count_touching_neighbors(
                                                                           touch_portion_within_range_neighbors_matrix))

        #print("count", all_stats["touch_portion_above_" + str(touch_portion_threshold) + "_neighbor_count"])


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

    # dilate label image and analye touching neighbors
    for dilation_radius in dilation_radii:
        dilated_label_image = dilate_labels(label_image, radius=dilation_radius)

        dilated_centroids = centroids_of_labels(dilated_label_image)
        # print("centroids:", centroids.shape)

        dilated_distance_matrix = generate_distance_matrix(dilated_centroids, dilated_centroids)
        # print("distance matrix", distance_matrix.shape)

        dilated_touch_matrix = generate_touch_matrix(dilated_label_image)
        # ignore touching background
        set_column(dilated_touch_matrix, 0, 0)
        set_row(dilated_touch_matrix, 0, 0)

        # print("touch matrix", touch_matrix)

        # touching_neighbor_count,
        all_stats["touching_neighbor_count_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                            data=count_touching_neighbors(dilated_touch_matrix))

        #minimum_distance_of_touching_neighbors,
        #average_distance_of_touching_neighbors,
        #maximum_distance_of_touching_neighbors,
        all_stats["minimum_distance_of_touching_neighbors_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                                           data=minimum_distance_of_touching_neighbors(
                                                                               dilated_distance_matrix, dilated_touch_matrix))
        all_stats["average_distance_of_touching_neighbors_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                                           data=average_distance_of_touching_neighbors(
                                                                               dilated_distance_matrix, dilated_touch_matrix))
        all_stats["maximum_distance_of_touching_neighbors_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                                           data=maximum_distance_of_touching_neighbors(
                                                                               dilated_distance_matrix, dilated_touch_matrix))

        #max_min_distance_ratio_of_touching_neighbor
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            all_stats["max_min_distance_ratio_of_touching_neighbors_dilated_r_" + str(dilation_radius)] = \
                all_stats["maximum_distance_of_touching_neighbors_dilated_r_" + str(dilation_radius)] / \
                all_stats["minimum_distance_of_touching_neighbors_dilated_r_" + str(dilation_radius)]

        # touch_count_sum
        # minimum_touch_count
        # maximum_touch_count
        # minimum_touch_portion
        # maximum_touch_portion

        # touch count
        dilated_touch_count_matrix = generate_touch_count_matrix(dilated_label_image)
        dilated_touch_portion_matrix = generate_touch_portion_matrix(dilated_label_image)
        # ignore touching background
        set_column(dilated_touch_count_matrix, 0, 0)
        set_row(dilated_touch_count_matrix, 0, 0)
        set_column(dilated_touch_portion_matrix, 0, 0)
        set_row(dilated_touch_portion_matrix, 0, 0)

        # To detect the minimum touch count/portion, we need to set all 0 pixels to a high value
        dilated_touch_count_matrix_0_set_to_high = replace_intensity(dilated_touch_count_matrix,
                                                             value_to_replace=0,
                                                             value_replacement=dilated_touch_count_matrix.max())

        temp = nan_to_num(dilated_touch_portion_matrix)
        dilated_touch_portion_matrix_0_set_to_high = replace_intensity(
            temp,
            value_to_replace=0,
            value_replacement=temp.max())

        all_stats["touch_count_sum_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True, data=sum_y_projection(dilated_touch_count_matrix))
        all_stats["minimum_touch_count_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                       data=minimum_y_projection(dilated_touch_count_matrix_0_set_to_high))
        all_stats["maximum_touch_count_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                        data=maximum_y_projection(dilated_touch_count_matrix))

        all_stats["minimum_touch_portion_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                         data=minimum_y_projection(dilated_touch_portion_matrix_0_set_to_high))
        all_stats["maximum_touch_portion_dilated_r_" + str(dilation_radius)] = cle_to_numpy(remove_first=True,
                                                          data=maximum_y_projection(dilated_touch_portion_matrix))

    return all_stats


def cle_to_numpy(data, remove_first=False):
    result = np.asarray(data)
    if len(result.shape) == 2:
        result = result[0]
    if remove_first:
        result = result[1:]
    return result
