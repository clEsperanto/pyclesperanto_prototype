import pyclesperanto_prototype as cle
import numpy as np

def test_copy_horizontal_slice_from_3d():

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
    cle.copy_horizontal_slice(test1, test2, 0)

    print(test2)
    a = cle.pull(test2)
    assert (np.min(a) == 1)
    assert (np.max(a) == 4)
    assert (np.mean(a) == 2.25)


def test_copy_horizontal_slice_to_3d():
    test1 = cle.push(np.asarray([
            [3, 4],
            [4, 5]
    ]))

    test2 = cle.create((2, 2, 2))
    cle.set(test2, 0)
    cle.copy_horizontal_slice(test1, test2, 0)

    print(test2)
    a = cle.pull(test2)
    assert (np.min(a) == 0)
    assert (np.max(a) == 5)
    assert (np.mean(a) == 2)

def test_copy_horizontal_slice_to_3d_b():
    test_image = cle.push(np.asarray([
        [
            [0,1,2],
            [3,4,5],
            [6,7,8],
        ],[
            [10,11,12],
            [13,14,15],
            [16,17,18],
        ],[
            [20,21,22],
            [23,24,25],
            [26,27,28],
        ]
    ]))

    reference = cle.push(np.asarray([
        [3,4,5],
        [13,14,15],
        [23,24,25]
    ]))

    result = cle.create([3,3])

    cle.copy_horizontal_slice(test_image, result, slice_index=1)

    print(reference)
    print(result)

    assert np.array_equal(reference, result)

