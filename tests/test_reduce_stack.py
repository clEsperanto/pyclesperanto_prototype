import pyclesperanto_prototype as cle
import numpy as np

def test_reduce_offset_0():

    test = cle.push(np.asarray([
        [
            [0, 0],
            [0, 5]
        ],
        [
            [1, 1],
            [1, 5]
        ],
        [
            [2, 2],
            [2, 5]
        ],
        [
            [3, 3],
            [3, 5]
        ],
    ]))

    ref = cle.push(np.asarray([
        [
            [0, 0],
            [0, 5]
        ],
        [
            [2, 2],
            [2, 5]
        ],
    ]))

    res = cle.reduce_stack(test, reduction_factor=2)

    a = cle.pull(res)
    b = cle.pull(ref)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))

def test_reduce_offset_1():

    test = cle.push(np.asarray([
        [
            [0, 0],
            [0, 5]
        ],
        [
            [1, 1],
            [1, 5]
        ],
        [
            [2, 2],
            [2, 5]
        ],
        [
            [3, 3],
            [3, 5]
        ],
    ]))

    ref = cle.push(np.asarray([
        [
            [1, 1],
            [1, 5]
        ],
    ]))

    res = cle.reduce_stack(test, reduction_factor=3, offset=1)

    a = cle.pull(res)
    b = cle.pull(ref)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))

