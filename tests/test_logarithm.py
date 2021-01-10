import pyclesperanto_prototype as cle
import numpy as np


def test_logarithm():
    test1 = cle.push(np.asarray([
        [1, 10],
        [1000, 100]
    ]))

    reference = cle.push(np.asarray([
        [0, 2.3026],
        [6.9078, 4.6052]
    ]))

    result = cle.create(test1)
    cle.logarithm(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.01))

