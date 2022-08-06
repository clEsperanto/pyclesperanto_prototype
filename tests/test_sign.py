
import numpy as np
import pyclesperanto_prototype as cle

def test_sign():
    data = np.asarray([[-np.inf],
                        [np.inf],
                        [0],
                        [1],
                       [-1],
                        [np.nan]])

    print(np.sign(data))
    print(cle.sign(data))

    # we exclude nan from the test, because numpy cannot compare it
    assert np.allclose(np.sign(data)[0:4],
                       cle.sign(data)[0:4])



