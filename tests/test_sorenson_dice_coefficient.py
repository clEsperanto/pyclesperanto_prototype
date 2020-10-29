import pyclesperanto_prototype as cle
import numpy as np


def test_sorensen_dice_coefficient_2d():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0]
    ]))

    test2 = cle.push(np.asarray([
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]))

    d = cle.sorensen_dice_coefficient(test1, test2)

    assert abs(d - 0.666) < 0.001
    print("ok sorensen_dice_coefficient")

def test_sorensen_dice_coefficient_3d():
    test1 = cle.push(np.asarray([
        [[0, 0, 0], [0, 0, 0]],
        [[0, 1, 1], [0, 1, 0]]
    ]))

    test2 = cle.push(np.asarray([
        [[0, 1, 1], [0, 1, 0]],
        [[0, 1, 1], [0, 1, 0]]
    ]))

    d = cle.sorensen_dice_coefficient(test1, test2)

    assert abs(d - 0.666) < 0.001
    print("ok sorensen_dice_coefficient")

