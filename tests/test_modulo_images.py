import pyclesperanto_prototype as cle
import numpy as np


def test_modulo_images():
    test = [[2, 5], [2, 3]]
    test_div = [[2, 2], [2, 2]]
    reference = [[0, 1], [0, 1]]

    result = cle.modulo_images(test, test_div)

    assert np.array_equal(result, reference)
