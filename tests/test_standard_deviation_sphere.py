import pyclesperanto_prototype as cle
import numpy as np

def test_standard_deviation_sphere():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0.4, 0, 0],
        [0, 0.4, 0.4, 0.4, 0],
        [0, 0, 0.4, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.standard_deviation_sphere(test1, result, 1, 1, 0)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.allclose(a, b, 0.01))
