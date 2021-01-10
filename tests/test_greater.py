import pyclesperanto_prototype as cle
import numpy as np


def test_greater_2d():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 3, 3, 4, 0],
        [0, 4, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))
    test2 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 3, 3, 3, 0],
        [0, 3, 3, 3, 0],
        [0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.greater(test1, test2, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    print(a)

    assert (np.array_equal(a, b))
    print("ok greater_or_equal")

def test_greater_3d():
    test1 = cle.push_zyx(np.asarray([
        [
            [0, 1, 2, 3, 0],
            [0, 3, 3, 4, 0]
        ],[
            [0, 4, 4, 5, 0],
            [0, 0, 0, 0, 0]
        ]
    ]))
    test2 = cle.push_zyx(np.asarray([
        [
            [0, 3, 3, 3, 0],
            [0, 3, 3, 3, 0],
        ], [
            [0, 3, 3, 3, 0],
            [0, 0, 0, 0, 0]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0]
        ], [
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
    ]))

    result = cle.create(test1)
    cle.greater(test1, test2, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    print(a)

    assert (np.array_equal(a, b))
    print("ok greater_or_equal")

