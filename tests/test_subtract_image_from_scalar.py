import pyclesperanto_prototype as cle
import numpy as np


def test_subtract_image_from_scalar():
    test1 = cle.push_zyx(np.asarray([
        [0, 0],
        [1, 1],
        [2, 2]
    ]))

    reference = cle.push_zyx(np.asarray([
        [5, 5],
        [4, 4],
        [3, 3]
    ]))

    result = cle.create(test1)
    cle.subtract_image_from_scalar(test1, result, 5)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)

    assert (np.array_equal(a, b))
    print("ok subtract_image_from_scalar")
