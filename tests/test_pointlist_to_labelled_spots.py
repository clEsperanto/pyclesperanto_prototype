import pyclesperanto_prototype as cle
import numpy as np


def test_pointlist_to_labelled_spots_2d():
    positions_and_values = cle.push_zyx(np.asarray([
        [0, 0, 2, 3, 5],
        [0, 1, 3, 2, 6]
    ]))


    reference = cle.push_zyx(np.asarray([
        [1, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0],
        [0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5]
    ]))

    result = cle.pointlist_to_labelled_spots(positions_and_values)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_pointlist_to_labelled_spots_3d():
    positions_and_values = cle.push_zyx(np.asarray([
        [0, 0, 2, 3, 5],
        [0, 1, 3, 2, 6],
        [0, 0, 0, 0, 1]
    ]))


    reference = cle.push_zyx(np.asarray([
        [
            [1, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0],
            [0, 0, 3, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ],[
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 5]
        ]
    ]))

    result = cle.pointlist_to_labelled_spots(positions_and_values)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
