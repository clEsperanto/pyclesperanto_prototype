import pyclesperanto_prototype as cle
import numpy as np


def test_deskew_y():
    source = np.zeros((5, 5, 5))
    source[1, 1, 1] = 1

    reference = np.zeros((4, 8, 5))
    reference[1, 5, 1] = 1

    result = cle.deskew_y(source, angle_in_degrees=30)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    print(a.shape)
    print(b.shape)

    assert (np.array_equal(a, b))


