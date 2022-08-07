import pyclesperanto_prototype as cle
import numpy as np

def test_cubic_root():
    test =      np.asarray([[125, 64]])
    reference = np.asarray([[5, 4]])

    result = cle.cubic_root(test)

    assert np.allclose(result, reference)