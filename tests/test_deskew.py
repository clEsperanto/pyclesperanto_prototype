import pyclesperanto_prototype as cle
import numpy as np


def test_deskew_y():
    source = np.zeros((10, 10, 10))
    source[1, 1, 1] = 1

    reference = np.zeros((5, 19, 10))
    reference[4, 2, 1] = 1

    result = cle.deskew_y(source, angle_in_degrees=30)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    print(a.shape)
    print(b.shape)

    assert (np.array_equal(a, b))


