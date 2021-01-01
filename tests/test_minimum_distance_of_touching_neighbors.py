import pyclesperanto_prototype as cle
import numpy as np

def test_minimum_distance_of_touching_neighbors():

    labels = cle.push_zyx(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 2, 3, 3],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2]
    ]))

    reference = cle.push_zyx(np.asarray(
                    [[0, 3.1274989, 2.933641,  2.933641]]
    ))

    centroids = cle.centroids_of_labels(labels)
    distance_matrix = cle.generate_distance_matrix(centroids, centroids)
    touch_matrix = cle.generate_touch_matrix(labels)

    minimum_distance_of_touching_neighbors = cle.minimum_distance_of_touching_neighbors(distance_matrix, touch_matrix)

    a = cle.pull_zyx(minimum_distance_of_touching_neighbors)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
