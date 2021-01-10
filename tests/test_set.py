import pyclesperanto_prototype as cle
import numpy as np


def test_set():
    result = cle.create((5, 5))

    reference = cle.push_zyx(np.asarray([
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3]
    ]))

    cle.set(result, 3)

    print(result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)
    assert (np.allclose(a, b, 0.001))
