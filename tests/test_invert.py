import pyclesperanto_prototype as cle
import numpy as np


def test_grreater_or_equal():
    test = cle.push_zyx(np.asarray([
        [0, -6, 0, -3, 0],
        [0, 1, 2, 3, 0],
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 6, 0, 3, 0],
        [0, -1, -2, -3, 0],
    ]))

    result = cle.create(test)
    cle.invert(test, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    print(a)

    assert (np.array_equal(a, b))

