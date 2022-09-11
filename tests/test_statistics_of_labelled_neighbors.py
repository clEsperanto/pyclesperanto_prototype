
def test_statistics_of_labelled_neighbors():
    import numpy as np
    import pyclesperanto_prototype as cle
    from skimage.io import imread
    import matplotlib.pyplot as plt
    import pandas as pd

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
