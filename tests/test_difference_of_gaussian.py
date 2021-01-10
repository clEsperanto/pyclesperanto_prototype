import pyclesperanto_prototype as cle
import numpy as np

def test_difference_of_gaussian():

    test = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test)
    cle.difference_of_gaussian(test, result, 1, 1, 0, 2, 2, 0)

    print(result)

    a = cle.pull_zyx(result)
    assert (np.min(a) < -1.15)
    assert (np.min(a) > -1.18)
    assert (np.max(a) > 11.9)
    assert (np.max(a) < 12)

