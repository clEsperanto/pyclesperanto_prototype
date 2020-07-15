import pyclesperanto_prototype as cle
import numpy as np


def test_copy_slice_to_3d():

    test1 = cle.push(np.asarray([
        [
            [1, 4],
            [0, 4]
        ],
        [
            [1, 3],
            [1, 2]
        ]
    ]))

    test2 = cle.create((2, 2))
    cle.copy_slice(test1, test2, 0)

    print(test2)
    a = cle.pull(test2)
    assert (np.min(a) == 0)
    assert (np.max(a) == 1)
    assert (np.mean(a) == 0.75)
    print ("ok copy slice from 3d")


def test_copy_slice_to_3d():
    test1 = cle.push(np.asarray([
            [4, 4],
            [4, 4]
    ]))

    test2 = cle.create((2, 2, 2))
    cle.set(test2, 0)
    cle.copy_slice(test1, test2, 0)

    print(test2)
    a = cle.pull(test2)
    assert (np.min(a) == 0)
    assert (np.max(a) == 4)
    assert (np.mean(a) == 2)
    print ("ok copy slice to 3d")
