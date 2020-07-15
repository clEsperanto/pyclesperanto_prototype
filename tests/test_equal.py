import pyclesperanto_prototype as cle
import numpy as np


def test_equal():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 2, 3, 4, 0],
        [0, 3, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))

    test2 = cle.push(np.asarray([
        [1, 1, 1, 1, 1],
        [1, 5, 4, 3, 1],
        [1, 4, 3, 2, 1],
        [1, 3, 4, 1, 1],
        [1, 1, 1, 1, 1]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.equal(test1, test2, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.array_equal(a, b))
    print("ok equal")
