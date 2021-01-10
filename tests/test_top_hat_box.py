import pyclesperanto_prototype as cle
import numpy as np

def test_top_hat_sphere():

    test = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 50, 50, 50, 0],
        [0, 50, 100, 50, 0],
        [0, 50, 50, 50, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test)
    cle.top_hat_box(test, result, 1, 1, 0)

    print(result)

    a = cle.pull_zyx(result)
    assert (np.min(a) == 0)
    assert (np.max(a) == 50)

