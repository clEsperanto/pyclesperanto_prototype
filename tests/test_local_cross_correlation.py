import pyclesperanto_prototype as cle
import numpy as np

def test_local_cross_correlation():

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

    reference = cle.push(np.asarray(
        [[0.,        0.35355344, 0.],
         [0.35355344, 0.7071069,  0.35355344],
        [0.,         0.35355344, 0.]]
    ))

    test2 = cle.create(test)
    cle.local_cross_correlation(test, test1, test2)

    print(test2)

    a = cle.pull(test2)
    b = cle.pull(reference)
    assert np.allclose(a, b, atol=0.001)
