import pyclesperanto_prototype as cle
import numpy as np


def test_maximum_image_and_scalar():
    test1 = cle.push(np.asarray([
        [0, 3, 4, 5, 0],
        [0, 2, 1, 6, 0],
        [0, 0, 8, 7, 0]
    ]))

    reference = cle.push(np.asarray([
        [2, 3, 4, 5, 2],
        [2, 2, 2, 6, 2],
        [2, 2, 8, 7, 2]
    ]))

    result = cle.create(test1)
    cle.maximum_image_and_scalar(test1, result, 2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))
    print("ok maximum_image_and_scalar")
