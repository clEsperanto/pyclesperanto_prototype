import pyclesperanto_prototype as cle
import numpy as np

def test_exclude_labels_out_of_size_range_2d():
    
    gpu_input = cle.push_zyx(np.asarray([
            [1, 1, 2, 0, 3, 3],
            [1, 1, 2, 0, 3, 3],
            [0, 0, 0, 0, 0, 0],
            [4, 4, 5, 6, 6, 6],
            [4, 4, 5, 6, 6, 6]
    ]))

    gpu_reference = cle.push_zyx(np.asarray([
            [1, 1, 0, 0, 2, 2],
            [1, 1, 0, 0, 2, 2],
            [0, 0, 0, 0, 0, 0],
            [3, 3, 0, 0, 0, 0],
            [3, 3, 0, 0, 0, 0]
    ]))

    gpu_output = cle.exclude_labels_out_of_size_range(gpu_input, gpu_input, min_size=4, max_size=5)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

