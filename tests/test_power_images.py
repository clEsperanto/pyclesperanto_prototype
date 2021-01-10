import pyclesperanto_prototype as cle
import numpy as np


def test_power_images():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0]
    ]))
    test2 = cle.push_zyx(np.asarray([
        [1, 0, 0, 0, 0],
        [1, 1, 2, 3, 0],
        [1, 1, 2, 3, 0],
        [1, 1, 2, 3, 0],
        [1, 0, 0, 0, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 1, 1, 1, 1],
        [0, 1, 4, 27, 1],
        [0, 4, 25, 216, 1],
        [0, 7, 64, 729, 1],
        [0, 1, 1, 1, 1]
    ]))

    result = cle.create(test1)
    cle.power_images(test1, test2, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    print(a)

    assert (np.allclose(a, b, 0.0001))
