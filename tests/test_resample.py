import pyclesperanto_prototype as cle
import numpy as np

def test_resample_downsample_2d():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 2, 2],
        [0, 0, 2, 2],
        [1, 1, 4, 4],
        [1, 1, 4, 4]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 2],
        [1, 4]
    ]))

    result = cle.resample(test1, factor_x=0.5, factor_y=0.5)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    assert (np.array_equal(a, b))

def test_resample_upsample_2d():
    test1 = cle.push_zyx(np.asarray([
        [0, 2],
        [1, 4]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 2, 2],
        [0, 0, 2, 2],
        [1, 1, 4, 4],
        [1, 1, 4, 4]
    ]))

    result = cle.resample(test1, factor_x=2, factor_y=2)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    assert (np.array_equal(a, b))

def test_resample_downsample_3d():
    test1 = cle.push_zyx(np.asarray([
        [
            [0, 0, 2, 2],
            [0, 0, 2, 2],
            [1, 1, 4, 4],
            [1, 1, 4, 4]
        ],[
            [0, 0, 2, 2],
            [0, 0, 2, 2],
            [1, 1, 4, 4],
            [1, 1, 4, 4]
        ],[
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5]
        ],[
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        [
            [0, 2],
            [1, 4]
        ], [
            [5, 5],
            [5, 5]
        ]
    ]))

    result = cle.resample(test1, factor_x=0.5, factor_y=0.5, factor_z=0.5)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    assert (np.array_equal(a, b))

def test_resample_upsample_3d():
    test1 = cle.push_zyx(np.asarray([
        [
            [0, 2],
            [1, 4]
        ], [
            [5, 5],
            [5, 5]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        [
            [0, 0, 2, 2],
            [0, 0, 2, 2],
            [1, 1, 4, 4],
            [1, 1, 4, 4]
        ], [
            [0, 0, 2, 2],
            [0, 0, 2, 2],
            [1, 1, 4, 4],
            [1, 1, 4, 4]
        ], [
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5]
        ], [
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5],
            [5, 5, 5, 5]
        ]

    ]))

    result = cle.resample(test1, factor_x=2, factor_y=2, factor_z=2)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)
    assert (np.array_equal(a, b))

