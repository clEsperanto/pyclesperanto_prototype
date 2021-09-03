import pyclesperanto_prototype as cle
import numpy as np

def test_exclude_labels_out_of_size_range_2d():
    
    gpu_input = cle.push(np.asarray([
            [1, 1, 2, 0, 3, 3],
            [1, 1, 2, 0, 3, 3],
            [0, 0, 0, 0, 0, 0],
            [4, 4, 5, 6, 6, 6],
            [4, 4, 5, 6, 6, 6]
    ]))

    gpu_reference = cle.push(np.asarray([
            [1, 1, 0, 0, 2, 2],
            [1, 1, 0, 0, 2, 2],
            [0, 0, 0, 0, 0, 0],
            [3, 3, 0, 0, 0, 0],
            [3, 3, 0, 0, 0, 0]
    ]))

    gpu_output = cle.exclude_labels_outside_size_range(gpu_input, gpu_input, minimum_size=4, maximum_size=5)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_exclude_small_labels_2d():
    gpu_input = cle.push(np.asarray([
        [1, 1, 2, 0, 3, 3],
        [1, 1, 2, 0, 3, 3],
        [0, 0, 0, 0, 0, 0],
        [4, 4, 5, 6, 6, 6],
        [4, 4, 5, 6, 6, 6]
    ]))

    gpu_reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1]
    ]))

    gpu_output = cle.exclude_small_labels(gpu_input, gpu_input, maximum_size=5)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_exclude_large_labels_2d():
    gpu_input = cle.push(np.asarray([
        [1, 1, 2, 0, 3, 3],
        [1, 1, 2, 0, 3, 3],
        [0, 0, 0, 0, 0, 0],
        [4, 4, 5, 6, 6, 6],
        [4, 4, 5, 6, 6, 6]
    ]))

    gpu_reference = cle.push(np.asarray([
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0],
        [0, 0, 2, 0, 0, 0]
    ]))



    gpu_output = cle.exclude_large_labels(gpu_input, gpu_input, minimum_size=3)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
