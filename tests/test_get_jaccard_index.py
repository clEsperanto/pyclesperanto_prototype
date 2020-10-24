import pyclesperanto_prototype as cle
import numpy as np


def test_get_jaccard_index_2d():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0]
    ]))

    test2 = cle.push(np.asarray([
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]))

    j = cle.get_jaccard_index(test1, test2)

    assert j == 0.5
    print("ok get_jaccard_index")

def test_get_jaccard_index_3d():
    test1 = cle.push(np.asarray([
        [[0, 0, 0], [0, 0, 0]],
        [[0, 1, 1], [0, 1, 0]]
    ]))

    test2 = cle.push(np.asarray([
        [[0, 1, 1], [0, 1, 0]],
        [[0, 1, 1], [0, 1, 0]]
    ]))

    j = cle.get_jaccard_index(test1, test2)

    assert j == 0.5
    print("ok get_jaccard_index")

