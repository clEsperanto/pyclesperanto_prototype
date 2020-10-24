import pyclesperanto_prototype as cle
import numpy as np
import pytest
import pyopencl as cl

def test_sum_of_all_pixels_3d():
    test1 = cle.push(np.asarray([
        [
            [0, 4, 0, 0, 2],
            [0, 0, 0, 8, 0],
            [3, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 2, 0, 0]
        ]
    ]))

    s = cle.sum_of_all_pixels(test1)

    assert s == 20


def test_sum_of_all_pixels_2d():
    test1 = cle.push(np.asarray([
            [0, 4, 0, 0, 2],
            [0, 0, 0, 8, 0],
            [3, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 2, 0, 0]
    ]))

    s = cle.sum_of_all_pixels(test1)

    assert s == 20

def test_sum_of_all_pixels_1d():
    test1 = cle.push(np.asarray(
            [0, 4, 0, 0, 2]
    ))

    s = cle.sum_of_all_pixels(test1)

    assert s == 6


def test_sum_of_all_pixels_1d_y():
    test1 = cle.push(np.asarray(
            [[0], [4], [0], [0], [2]]
    ))

    s = cle.sum_of_all_pixels(test1)

    assert s == 6

def test_sum_of_all_pixels_1d_z():
    test1 = cle.push(np.asarray(
            [[[0]], [[4]], [[0]], [[0]], [[2]]]
    ))

    s = cle.sum_of_all_pixels(test1)

    assert s == 6
