import pyclesperanto_prototype as cle
import numpy as np

def test_average_neighbor_distance_map():

    labels = cle.push(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2]
    ]))

    reference = cle.push(np.asarray([
                    [3, 3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3, 3],
                    [0, 0, 0, 3, 3, 3],
                    [0, 0, 0, 3, 3, 3],
                    [0, 0, 0, 3, 3, 3]
    ]))


    average_distance_of_touching_neighbors_map = cle.average_neighbor_distance_map(labels)

    a = cle.pull(average_distance_of_touching_neighbors_map)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
