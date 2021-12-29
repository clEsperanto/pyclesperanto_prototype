import pyclesperanto_prototype as cle
import numpy as np

def test_average_distance_of_n_shortest_distances():

    labels = cle.push(np.asarray([
                    [1, 0, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2]
    ]))

    other_labels = cle.push(np.asarray([
                    [0, 2, 0, 0, 0, 3],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 4],
                    [0, 0, 0, 0, 5, 0]
    ]))


    reference = cle.push(np.asarray(
                    [0, 1, 1, 0]
    ))

    centroids_a = cle.centroids_of_labels(labels)
    centroids_b = cle.centroids_of_labels(other_labels)
    print(centroids_a)
    print(centroids_b)
    distance_matrix = cle.generate_distance_matrix(centroids_a, centroids_b)
    print(distance_matrix)

    average_distance_to_n_nearest_distance = cle.average_distance_of_n_nearest_distances(distance_matrix, n=1)

    a = cle.pull(average_distance_to_n_nearest_distance)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
