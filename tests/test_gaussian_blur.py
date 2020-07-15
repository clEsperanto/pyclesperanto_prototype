import pyclesperanto_prototype as cle
import numpy as np


def test_gaussian_blur():

    test = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test)
    cle.gaussian_blur(test, result, 1, 1, 0)

    print(result)

    a = cle.pull(result)
    assert (np.min(a) > 0)
    assert (np.max(a) > 15.9)
    assert (np.max(a) < 16)

    print ("ok gaussian_blur")
    