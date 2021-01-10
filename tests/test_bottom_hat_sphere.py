import pyclesperanto_prototype as cle
import numpy as np

def test_bottom_hat_sphere():

    test = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 50, 50, 50, 0],
        [0, 50, 100, 50, 0],
        [0, 50, 50, 50, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test)
    cle.bottom_hat_sphere(test, result, 1, 1, 0)

    print(result)

    a = cle.pull(result)
    assert (np.min(a) == 0)
    assert (np.max(a) == 50)

