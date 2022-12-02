
def test_statistics_of_labelled_neighbors():
    import numpy as np
    import pyclesperanto_prototype as cle

    labels = cle.scale(cle.asarray([
        [1, 1, 2, 2, 3, 3, 3, 3],
        [1, 1, 2, 2, 3, 3, 3, 3],
        [1, 1, 7, 7, 7, 7, 3, 3],
        [1, 1, 7, 7, 7, 7, 3, 3],
        [6, 6, 7, 7, 7, 7, 4, 4],
        [6, 6, 7, 7, 7, 7, 4, 4],
        [5, 5, 5, 5, 5, 5, 4, 4],
        [5, 5, 5, 5, 5, 5, 4, 4],
    ]), factor_x=10, factor_y=10, auto_size=True).astype(np.uint32)

    distance_mesh = cle.draw_distance_mesh_between_touching_labels(labels)

    assert abs(distance_mesh.max() - 43.843155) < 0.001

    stats = cle.statistics_of_labelled_neighbors(labels)

    assert abs(stats["label"].tolist()[-1] - 7) < 0.001
    assert abs(stats["touching_neighbor_count"].tolist()[-1] - 6) < 0.001
    assert abs(stats["maximum_distance_of_touching_neighbors"].max() - 43.843155) < 0.001
    assert abs(stats["average_distance_of_touching_neighbors"].tolist()[-1] - 33.329612731933594) < 0.001
    assert abs(stats["minimum_distance_of_touching_neighbors"].tolist()[-1] - 31.62277603149414) < 0.001
    assert abs(stats["maximum_distance_of_touching_neighbors"].tolist()[-1] - 36.055511474609375) < 0.001
    assert abs(stats["proximal_neighbor_count_d20"].tolist()[-1] - 0) < 0.001
    assert abs(stats["proximal_neighbor_count_d40"].tolist()[-1] - 6) < 0.001
    assert abs(stats["maximum_distance_of_n1_nearest_neighbors"].tolist()[-1] - 31.62277603149414) < 0.001
    assert abs(stats["maximum_distance_of_n2_nearest_neighbors"].tolist()[-1] - 31.62277603149414) < 0.001
    assert abs(stats["maximum_distance_of_n3_nearest_neighbors"].tolist()[-1] - 31.62277603149414) < 0.001
    assert abs(stats["maximum_distance_of_n4_nearest_neighbors"].tolist()[-1] - 32.99831771850586) < 0.001
    assert abs(stats["maximum_distance_of_n5_nearest_neighbors"].tolist()[-1] - 36.055511474609375) < 0.001
    assert abs(stats["maximum_distance_of_n6_nearest_neighbors"].tolist()[-1] - 36.055511474609375) < 0.001
    assert abs(stats["touch_count_sum"].tolist()[-1] - 160) < 0.001
    assert abs(stats["minimum_touch_count"].tolist()[-1] - 20) < 0.001
    assert abs(stats["maximum_touch_count"].tolist()[-1] - 40) < 0.001
    assert abs(stats["minimum_touch_portion"].tolist()[-1] - 0.125) < 0.001
    assert abs(stats["maximum_touch_portion"].tolist()[-1] - 0.25) < 0.001
    assert abs(stats["touch_portion_above_0_neighbor_count"].tolist()[-1] - 6) < 0.001
    assert abs(stats["touch_portion_above_0.16_neighbor_count"].tolist()[-1] - 2) < 0.001
    assert abs(stats["touch_portion_above_0.2_neighbor_count"].tolist()[-1] - 2) < 0.001
    assert abs(stats["touch_portion_above_0.33_neighbor_count"].tolist()[-1] - 0) < 0.001
    assert abs(stats["touch_portion_above_0.5_neighbor_count"].tolist()[-1] - 0) < 0.001
    assert abs(stats["touch_portion_above_0.75_neighbor_count"].tolist()[-1] - 0) < 0.001

def test_statistics_of_labelled_neighbors_dilated():
    import numpy as np
    import pyclesperanto_prototype as cle

    labels = cle.scale(cle.asarray([
        [0, 1, 2, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 7, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0],
    ]), factor_x=2, factor_y=2, auto_size=True).astype(np.uint32)

    stats = cle.statistics_of_labelled_neighbors(labels, dilation_radii=(0, 10))

    assert np.all(stats["touching_neighbor_count_dilated_r_0"] == stats["touching_neighbor_count"])
    assert np.all(stats["minimum_distance_of_touching_neighbors_dilated_r_0"] == stats["minimum_distance_of_touching_neighbors"])
    assert np.all(stats["average_distance_of_touching_neighbors_dilated_r_0"] == stats["average_distance_of_touching_neighbors"])
    assert np.all(stats["maximum_distance_of_touching_neighbors_dilated_r_0"] == stats["maximum_distance_of_touching_neighbors"])
    for i,j in zip(stats["max_min_distance_ratio_of_touching_neighbors_dilated_r_0"].tolist(), stats["max_min_distance_ratio_of_touching_neighbors"].tolist()):
        assert i == j or (np.isnan(i) and np.isnan(j))

    assert np.all(stats["touch_count_sum_dilated_r_0"] == stats["touch_count_sum"])
    assert np.all(stats["minimum_touch_count_dilated_r_0"] == stats["minimum_touch_count"])
    assert np.all(stats["maximum_touch_count_dilated_r_0"] == stats["maximum_touch_count"])
    assert np.all(stats["minimum_touch_portion_dilated_r_0"] == stats["minimum_touch_portion"])
    assert np.all(stats["maximum_touch_portion_dilated_r_0"] == stats["maximum_touch_portion"])

    assert np.any(stats["touching_neighbor_count_dilated_r_10"] > stats["touching_neighbor_count"])
    assert np.any(stats["minimum_distance_of_touching_neighbors_dilated_r_10"] > stats["minimum_distance_of_touching_neighbors"])
    assert np.any(stats["average_distance_of_touching_neighbors_dilated_r_10"] > stats["average_distance_of_touching_neighbors"])
    assert np.any(stats["maximum_distance_of_touching_neighbors_dilated_r_10"] > stats["maximum_distance_of_touching_neighbors"])
    assert np.any(stats["max_min_distance_ratio_of_touching_neighbors_dilated_r_10"] > stats["max_min_distance_ratio_of_touching_neighbors"])
    assert np.any(stats["touch_count_sum_dilated_r_10"] > stats["touch_count_sum"])
    assert np.any(stats["minimum_touch_count_dilated_r_10"] > stats["minimum_touch_count"])
    assert np.any(stats["maximum_touch_count_dilated_r_10"] > stats["maximum_touch_count"])
    assert np.any(stats["minimum_touch_portion_dilated_r_10"] != stats["minimum_touch_portion"])
    assert np.any(stats["maximum_touch_portion_dilated_r_10"] > stats["maximum_touch_portion"])
