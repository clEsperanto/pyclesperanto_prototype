import pyclesperanto_prototype as cle
import numpy as np

def test_flag_existing_labels():

    gpu_input = cle.push(np.asarray([
        [
            [1, 2, 3],
            [1, 6, 6],
            [7, 8, 9]
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 1]
    ]))

    gpu_output = cle.flag_existing_labels(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))