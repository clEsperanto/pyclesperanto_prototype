import pyclesperanto_prototype as cle
import numpy as np

def test_proximal_other_labels_count_map():

    labels = cle.push(np.asarray([
                    [1, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0],
                    [4, 0, 0, 0, 5]
    ]))

    other_labels = cle.push(np.asarray([
                    [1, 2, 0, 0, 4],
                    [3, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0],
                    [8, 8, 0, 0, 7],
                    [8, 8, 0, 0, 6]
    ]))


    reference = cle.push(np.asarray([
        [0, 3, 0, 2, 1, 2],
    ]))

    touching_other_labels_count = cle.proximal_other_labels_count(labels, other_labels, maximum_distance=1)

    a = cle.pull(touching_other_labels_count)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.array_equal(a, b))
