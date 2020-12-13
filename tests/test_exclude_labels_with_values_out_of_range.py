import pyclesperanto_prototype as cle
import numpy as np

def test_exclude_labels_with_values_out_of_range_2d():
    
    gpu_input = cle.push_zyx(np.asarray([

            [0, 1, 2, 3, 4, 5, 6]

    ]))

    gpu_reference = cle.push_zyx(np.asarray([

            [0, 1, 2, 3, 0, 0, 0]

    ]))

    gpu_output = cle.exclude_labels_with_values_out_of_range(gpu_input, gpu_input, minimum_value_range=0, maximum_value_range=3)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

