import pyclesperanto_prototype as cle
import numpy as np


def test_divide_images():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 4, 6, 8, 0],
        [0, 4, 6, 8, 0],
        [0, 4, 6, 8, 0],
        [0, 0, 0, 0, 0]
    ]))

    test2 = cle.push_zyx(np.asarray([
        [1, 1, 1, 1, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 2, 2, 4, 0],
        [0, 2, 2, 4, 0],
        [0, 4, 6, 8, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.divide_images(test1, test2, result)

    print(result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    assert (np.allclose(a, b, 0.0001))
