import pyclesperanto_prototype as cle
import numpy as np

def test_minimum_z_projection():
    test1 = cle.push_zyx(np.asarray([
        [
            [1, 0, 0, 0, 1],
            [0, 2, 0, 8, 1],
            [3, 0, 1, 0, 1],
            [0, 4, 0, 7, 1],
            [1, 1, 1, 1, 1]
        ], [
            [0, 2, 0, 8, 1],
            [1, 0, 0, 0, 1],
            [3, 0, 1, 0, 1],
            [0, 4, 0, 7, 1],
            [1, 1, 1, 1, 1]
        ], [
            [0, 2, 0, 8, 1],
            [3, 0, 1, 0, 1],
            [0, 4, 0, 7, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ], [
            [0, 2, 0, 8, 1],
            [1, 0, 0, 0, 1],
            [0, 4, 0, 7, 1],
            [3, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ], [
            [1, 0, 0, 0, 1],
            [0, 4, 0, 7, 1],
            [3, 0, 1, 0, 1],
            [0, 2, 0, 8, 1],
            [1, 1, 1, 1, 1]
        ]
    ]).T)

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
    ]).T)

    result = cle.create(reference)
    cle.minimum_z_projection(test1, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)

    assert (np.allclose(a, b, 0.001))
