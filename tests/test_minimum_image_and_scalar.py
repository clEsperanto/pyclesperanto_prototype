import pyclesperanto_prototype as cle
import numpy as np


def test_minimum_image_and_scalar():
    test1 = cle.push(np.asarray([
        [0, 3, 4, 5, 0],
        [0, 2, 1, 6, 0],
        [0, 0, 8, 7, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 2, 2, 2, 0],
        [0, 2, 1, 2, 0],
        [0, 0, 2, 2, 0]
    ]))

    result = cle.create(test1)
    cle.minimum_image_and_scalar(test1, result, 2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))


