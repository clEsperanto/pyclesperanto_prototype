import pyclesperanto_prototype as cle
import numpy as np


def test_write_values_to_positions_2d():
    positions_and_values = cle.push_zyx(np.asarray([
        [0, 0, 2, 3, 5],
        [0, 1, 3, 2, 6],
        [8, 7, 6, 5, 4]
    ]))


    reference = cle.push_zyx(np.asarray([
        [8, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0],
        [0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4]
    ]))

    result = cle.write_values_to_positions(positions_and_values)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_write_values_to_positions_3d():
    positions_and_values = cle.push_zyx(np.asarray([
        [0, 0, 2, 3, 5],
        [0, 1, 3, 2, 6],
        [0, 0, 0, 0, 1],
        [8, 7, 6, 5, 4]
    ]))


    reference = cle.push_zyx(np.asarray([
        [
            [8, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 0],
            [0, 0, 6, 0, 0, 0],
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
            [0, 0, 0, 0, 0, 4]
        ]
    ]))

    result = cle.write_values_to_positions(positions_and_values)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
