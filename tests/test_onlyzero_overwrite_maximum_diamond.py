import pyclesperanto_prototype as cle
import numpy as np


def onlyzero_overwrite_maximum_diamond():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 2, 3, 4, 0],
        [0, 4, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 1, 2, 3, 0],
        [1, 1, 2, 3, 3],
        [2, 2, 3, 4, 4],
        [4, 4, 4, 5, 5],
        [0, 4, 4, 5, 0]
    ]))

    result = cle.create(test1)
    flag = cle.create((1, 1, 1))
    cle.onlyzero_overwrite_maximum_diamond(test1, flag, result)

    print(result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    assert (np.array_equal(a, b))
