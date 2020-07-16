import pyclesperanto_prototype as cle
import numpy as np


def test_minimum_z_projection():
    test1 = cle.push(np.asarray([
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
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
    ]))

    result = cle.create(reference)
    cle.minimum_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.allclose(a, b, 0.001))
    print("ok minimum_z_projection")

