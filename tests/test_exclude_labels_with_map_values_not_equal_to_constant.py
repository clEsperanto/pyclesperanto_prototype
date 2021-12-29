import pyclesperanto_prototype as cle
import numpy as np

def test_exclude_labels_with_map_values_not_equal_to_constant_2d():
    
    gpu_input = cle.push(np.asarray([

            [0, 1, 2, 3, 4, 5, 6]

    ]))

    gpu_reference = cle.push(np.asarray([

            [0, 0, 0, 1, 0, 0, 0]

    ]))

    gpu_output = cle.exclude_labels_with_map_values_not_equal_to_constant(gpu_input, gpu_input, constant=3)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

