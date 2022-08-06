import pyclesperanto_prototype as cle
import numpy as np

def test_square_root():
    test =      np.asarray([[25, 16]])
    reference = np.asarray([[5, 4]])

    result = cle.square_root(test)

    assert np.allclose(result, reference)