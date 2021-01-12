import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_distance_of_touching_neighbors():

    labels = cle.push(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 2, 3, 3],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2]
    ]))

    reference = cle.push(np.asarray(
                    [[0, 4.031129,  4.031129,  3.1274989]]
    ))

    centroids = cle.centroids_of_labels(labels)
    distance_matrix = cle.generate_distance_matrix(centroids, centroids)
    touch_matrix = cle.generate_touch_matrix(labels)

    maximum_distance_of_touching_neighbors = cle.maximum_distance_of_touching_neighbors(distance_matrix, touch_matrix)

    a = cle.pull(maximum_distance_of_touching_neighbors)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
