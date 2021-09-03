import pyclesperanto_prototype as cle
import numpy as np

def test_touching_neighbor_count_map():

    labels = cle.push(np.asarray([
                    [1, 1, 0, 3, 3],
                    [1, 1, 2, 3, 3],
                    [0, 2, 2, 2, 0],
                    [4, 4, 2, 5, 5],
                    [4, 4, 0, 5, 5]
    ]))

    reference = cle.push(np.asarray([
        [1, 1, 0, 1, 1],
        [1, 1, 4, 1, 1],
        [0, 4, 4, 4, 0],
        [1, 1, 4, 1, 1],
        [1, 1, 0, 1, 1]
    ]))


    touching_neighbor_count_map = cle.touching_neighbor_count_map(labels)

    a = cle.pull(touching_neighbor_count_map)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.array_equal(a, b))
