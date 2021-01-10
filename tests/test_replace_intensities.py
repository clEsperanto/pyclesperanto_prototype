import pyclesperanto_prototype as cle
import numpy as np


def test_replace_intensities():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 2, 3, 4, 0],
        [0, 4, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))

    test2 = cle.push_zyx(np.asarray([
        [0, 9, 8, 7, 6, 5]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 9, 8, 7, 0],
        [0, 8, 7, 6, 0],
        [0, 6, 6, 5, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.replace_intensities(test1, test2, result)

    print(result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    assert (np.allclose(a, b, 0.001))
