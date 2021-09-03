import pyclesperanto_prototype as cle
import numpy as np

def test_convolve_fft():

    test = cle.push(np.asarray([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))

    test1 = cle.push(np.asarray([
        [0, 1, 0],
        [1, 2, 1],
        [0, 1, 0]
    ]))

    test2 = cle.create(test)
    cle.convolve_fft(test, test1, test2)

    print(test2)

    a = cle.pull(test1)
    b = cle.pull(test2)
    assert np.allclose(np.min(a), np.min(b), atol=0.001)
    assert np.allclose(np.max(a), np.max(b), atol=0.001)
    assert np.allclose(np.mean(a), np.mean(b), atol=0.001)
