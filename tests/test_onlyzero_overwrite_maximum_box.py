import pyclesperanto_prototype as cle
import numpy as np


def test_onlyzero_overwrite_maximum_box():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 2, 3, 4, 0],
        [0, 4, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [1, 2, 3, 3, 3],
        [2, 1, 2, 3, 4],
        [4, 2, 3, 4, 5],
        [4, 4, 4, 5, 5],
        [4, 4, 5, 5, 5]
    ]))

    result = cle.create(test1)
    flag = cle.create((1, 1, 1))
    cle.onlyzero_overwrite_maximum_box(test1, flag, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.array_equal(a, b))
    print("ok onlyzero_overwrite_maximum_box")