import pyclesperanto_prototype as cle
import numpy as np


def test_square():
    test1 = cle.push(np.asarray([
        [4, 5]
    ]))

    reference = cle.push(np.asarray([
        [16, 25]
    ]))

    result = cle.square(test1)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.allclose(a, b, 0.001))
