import pyclesperanto_prototype as cle
import numpy as np


def test_clip_min_max():
    test = [[0, 1], [2, 3]]
    reference = [[1, 1], [2, 2]]

    result = cle.clip(test, a_min=1, a_max=2)

    assert np.array_equal(result, reference)

def test_clip_max():
    test = [[0, 1], [2, 3]]
    reference = [[0, 1], [2, 2]]

    result = cle.clip(test, a_max=2)

    assert np.array_equal(result, reference)

def test_clip_min():
    test = [[0, 1], [2, 3]]
    reference = [[1, 1], [2, 3]]

    result = cle.clip(test, a_min=1)

    assert np.array_equal(result, reference)
