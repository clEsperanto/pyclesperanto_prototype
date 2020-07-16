import pyclesperanto_prototype as cle
import numpy as np


def test_equal_constant():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 2, 3, 4, 0],
        [0, 4, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.equal_constant(test1, result, 4)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.array_equal(a, b))
    print("ok equal_constant")
