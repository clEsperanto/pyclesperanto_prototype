import pyclesperanto_prototype as cle
import numpy as np
import pytest
import pyopencl as cl

from . import LINUX, CI

@pytest.mark.xfail('LINUX and CI', reason='INVALID_ARG_SIZE on CI', raises=cl.LogicError)
def test_copy_slice_from_3d():

    test1 = cle.push(np.asarray([
        [
            [1, 4],
            [0, 4]
        ],
        [
            [1, 3],
            [1, 2]
        ]
    ]))

    test2 = cle.create((2, 2))
    cle.copy_slice(test1, test2, 0)

    print(test2)
    a = cle.pull(test2)
    assert (np.min(a) == 0)
    assert (np.max(a) == 1)
    assert (np.mean(a) == 0.75)
    print ("ok copy slice from 3d")


@pytest.mark.xfail(reason="BUILD_PROGRAM_FAILURE")
def test_copy_slice_to_3d():
    test1 = cle.push(np.asarray([
            [3, 4],
            [4, 5]
    ]))

    test2 = cle.create((2, 2, 2))
    cle.set(test2, 0)
    cle.copy_slice(test1, test2, 0)

    print(test2)
    a = cle.pull(test2)
    assert (np.min(a) == 0)
    assert (np.max(a) == 4)
    assert (np.mean(a) == 2)
    print ("ok copy slice to 3d")

def test_copy_slice_to3d_with_one_slice():
    test1 = cle.push(np.asarray([
        [3, 4, 6],
        [4, 5, 2]
    ]))

    print(test1)
    print("shape test1 " + str(test1.shape))

    test2 = cle.create((1, 3, 2))
    print("shape test2 " + str(test2.shape))
    print(test2)

    cle.copy_slice(test1, test2, 0)
    print(test2)

    a = cle.pull(test2)
    assert (np.min(a) == 2)
    assert (np.max(a) == 6)
    assert (np.mean(a) == 4)

def test_copy_slice_to3d_with_one_slice_zyx():
    test1 = cle.push_zyx(np.asarray([
        [3, 4, 6],
        [4, 5, 2]
    ]))

    print(test1)
    print("shape test1 " + str(test1.shape))

    test2 = cle.create_zyx((1, 3, 2))
    print("shape test2 " + str(test2.shape))
    print(test2)

    cle.copy_slice(test1, test2, 0)
    print(test2)

    a = cle.pull(test2)
    assert (np.min(a) == 2)
    assert (np.max(a) == 6)
    assert (np.mean(a) == 4)