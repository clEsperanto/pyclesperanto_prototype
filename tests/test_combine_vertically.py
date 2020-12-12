import pyclesperanto_prototype as cle
import numpy as np


def test_combine_vertically():
    test1 = cle.push_zyx(np.asarray([
        [1, 1],
        [1, 1]
    ]))
    test2 = cle.push_zyx(np.asarray([
        [2, 2],
        [2, 2]
    ]))

    reference = cle.push_zyx(np.asarray([
        [1, 1],
        [1, 1],
        [2, 2],
        [2, 2]
    ]))

    result = cle.combine_vertically(test1, test2)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.01))

