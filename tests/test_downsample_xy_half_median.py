import pyclesperanto_prototype as cle
import numpy as np

def test_downsample_xy_by_half_median():
    test1 = cle.push(np.asarray([
        [-3, 0, 1, 2],
        [0, 5, 2, 7],
        [0, 1, 3, 4],
        [1, 6, 4, 8]
    ]))

    reference = cle.push(np.asarray([
        [0, 2],
        [1, 4]
    ]))

    result = cle.downsample_slice_by_slice_half_median(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    assert (np.array_equal(a, b))

def test_resample_downsample_3d():
    test1 = cle.push(np.asarray([
        [
            [-3, 0, 1, 2],
            [0, 5, 2, 7],
            [0, 1, 3, 4],
            [1, 6, 4, 8]
        ],[
            [-3, 0, 1, 2],
            [0, 5, 2, 7],
            [0, 1, 3, 4],
            [1, 6, 4, 8]
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

    reference = cle.push(np.asarray([
        [
            [0, 2],
            [1, 4]
        ], [
            [0, 2],
            [1, 4]
        ], [
            [5, 5],
            [5, 5]
        ], [
            [5, 5],
            [5, 5]
        ]
    ]))

    result = cle.downsample_slice_by_slice_half_median(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    assert (np.array_equal(a, b))
