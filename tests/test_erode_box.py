import pyclesperanto_prototype as cle
import numpy as np


def test_erode_box():
    test = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test)
    cle.erode_box(test, result)

    print(result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    assert (np.array_equal(a, b))
