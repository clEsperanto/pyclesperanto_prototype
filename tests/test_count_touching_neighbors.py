import pyclesperanto_prototype as cle
import numpy as np

def test_count_touching_neighbors():

    labels = cle.push_zyx(np.asarray([
                    [1, 1, 0, 3, 3],
                    [1, 1, 2, 3, 3],
                    [0, 2, 2, 2, 0],
                    [4, 4, 2, 5, 5],
                    [4, 4, 0, 5, 5]
    ]))

    reference = cle.push_zyx(np.asarray(
                    [[5, 2, 5, 2, 2, 2]]
    ))

    touch_matrix = cle.generate_touch_matrix(labels)

    neighbor_count_vector = cle.count_touching_neighbors(touch_matrix)

    a = cle.pull_zyx(neighbor_count_vector)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)


    assert (np.array_equal(a, b))
