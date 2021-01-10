import pyclesperanto_prototype as cle
import numpy as np


def test_multiply_images():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0]
    ]))
    test2 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 2, 2, 2, 0],
        [0, 1, 1, 1, 0],
        [0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 2, 4, 6, 0],
        [0, 4, 5, 6, 0],
        [0, 21, 24, 27, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.multiply_images(test1, test2, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    print(a)

    assert (np.array_equal(a, b))
