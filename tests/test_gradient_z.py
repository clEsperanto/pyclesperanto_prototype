import pyclesperanto_prototype as cle
import numpy as np
import pytest
import pyopencl as cl


@pytest.mark.xfail(raises=cl.RuntimeError)
def test_gradient_z():
    test = cle.push_zyx(np.asarray([
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, -1, 0],
            [1, 0, 0, -1, 0],
            [1, 0, 0, -1, 0],
            [0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0],
            [-1, 0, 0, 1, 0],
            [-1, 0, 0, 1, 0],
            [-1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
    ]))

    result = cle.create(test)
    cle.gradient_z(test, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)

    assert (np.array_equal(a, b))

