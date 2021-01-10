import pyclesperanto_prototype as cle
import numpy as np


def test_gradient_y():
    test = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 1, 3, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 1, 2, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 0, 1, 0, 0],
        [0, -1, -2, 0, 0],
        [0, -1, -3, 0, 0]
    ]))

    result = cle.create(test)
    cle.gradient_y(test, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    print(a)

    assert (np.array_equal(a, b))

