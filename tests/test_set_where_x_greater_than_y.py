import pyclesperanto_prototype as cle
import numpy as np


def test_set_where_x_greater_than_y():
    result = cle.push_zyx(np.asarray([
        [0, 0, 0, 1],
        [0, 0, 3, 1],
        [0, 0, 3, 1],
        [1, 1, 1, 1]
    ]).T)

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 1],
        [3, 0, 3, 1],
        [3, 3, 3, 1],
        [3, 3, 3, 1]
    ]).T)

    cle.set_where_x_greater_than_y(result, 3)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    print(a)

    assert (np.array_equal(a, b))
