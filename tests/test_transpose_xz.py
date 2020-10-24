import pyclesperanto_prototype as cle
import numpy as np
import pytest
import pyopencl as cl


@pytest.mark.xfail(raises=cl.RuntimeError)
def test_transpose_xz():
    test1 = cle.push(np.asarray([
        [
            [0, 1],
            [2, 3]
        ], [
            [4, 5],
            [6, 7]
        ]
    ]))

    reference = cle.push(np.asarray([
        [
            [0, 4],
            [2, 6]
        ], [
            [1, 5],
            [3, 7]
        ]
    ]))

    result = cle.create(test1)
    cle.transpose_xz(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))
    print("ok transpose_xz")

def test_transpose_xz_3d_generate_output():
    test1 = cle.push(np.asarray([
        [
            [1, 2, 6],
            [3, 4, 5]
        ]
    ]))

    result = cle.transpose_xz(test1)

    a = cle.pull(result)

    assert (np.min(a) == 1)
    assert (np.max(a) == 6)
    assert (np.mean(a) == 3.5)

def test_transpose_xz_2d_generate_output():
    test1 = cle.push(np.asarray([
            [1, 2, 6],
            [3, 4, 5]
    ]))

    result = cle.transpose_xz(test1)

    a = cle.pull(result)

    print(a)

    assert (np.min(a) == 1)
    assert (np.max(a) == 6)
    assert (np.mean(a) == 3.5)

def test_transpose_xz_1d_generate_output():
    test1 = cle.push(np.asarray(
            [1, 2, 6, 3, 4, 5]
    ))

    result = cle.transpose_xz(test1)

    a = cle.pull(result)

    print(a)

    assert (np.min(a) == 1)
    assert (np.max(a) == 6)
    assert (np.mean(a) == 3.5)
