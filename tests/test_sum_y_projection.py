import pyclesperanto_prototype as cle
import numpy as np

def test_sum_y_projection():
    test1 = cle.push_zyx(np.asarray([
        [
            [1, 0, 0, 0, 9],
            [0, 2, 0, 8, 0],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [5, 0, 6, 0, 10]
        ], [
            [0, 2, 0, 8, 0],
            [1, 0, 0, 0, 9],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [5, 0, 6, 0, 10]
        ], [
            [0, 2, 0, 8, 0],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [1, 0, 0, 0, 9],
            [5, 0, 6, 0, 10]
        ], [
            [0, 2, 0, 8, 0],
            [1, 0, 0, 0, 9],
            [0, 4, 0, 7, 0],
            [3, 0, 1, 0, 10],
            [5, 0, 6, 0, 10]
        ], [
            [1, 0, 0, 0, 9],
            [0, 4, 0, 7, 0],
            [3, 0, 1, 0, 10],
            [0, 2, 0, 8, 0],
            [5, 0, 6, 0, 10]
        ]
    ]).T)

    reference = cle.push_zyx(np.asarray([
        [9, 6, 7, 15, 29],
        [9, 6, 7, 15, 29],
        [9, 6, 7, 15, 29],
        [9, 6, 7, 15, 29],
        [9, 6, 7, 15, 29]
    ]).T)

    result = cle.create(reference)
    cle.sum_y_projection(test1, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)

    assert (np.allclose(a, b, 0.01))
