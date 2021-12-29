import pyclesperanto_prototype as cle
import numpy as np

def test_average_distance_of_n_nearest_neighbors_map():

    labels = cle.push(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2]
    ]))

    reference = cle.push(np.asarray([
                    [3.62, 3.62, 3.62, 3, 3, 3],
                    [3.62, 3.62, 3.62, 3, 3, 3],
                    [3.62, 3.62, 3.62, 3, 3, 3],
                    [0, 0, 0, 3.62, 3.62, 3.62],
                    [0, 0, 0, 3.62, 3.62, 3.62],
                    [0, 0, 0, 3.62, 3.62, 3.62]
    ]))

    average_distance_of_n_nearest_neighbors_map = cle.average_distance_of_n_closest_neighbors_map(labels, n=2)

    a = cle.pull(average_distance_of_n_nearest_neighbors_map)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
