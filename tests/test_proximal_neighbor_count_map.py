import pyclesperanto_prototype as cle
import numpy as np

def test_proximal_neighbor_count_map():

    labels = cle.push(np.asarray([
                    [1, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0],
                    [4, 0, 0, 0, 5]
    ]))

    reference = cle.push(np.asarray([
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ]))


    touching_neighbor_count_map = cle.proximal_neighbor_count_map(labels, min_distance=0, max_distance=3)

    a = cle.pull(touching_neighbor_count_map)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.array_equal(a, b))
