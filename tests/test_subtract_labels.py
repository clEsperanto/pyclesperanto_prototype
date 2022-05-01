import pyclesperanto_prototype as cle
import numpy as np

def test_subtract_labels_2d():

    gpu_input1 = cle.push(np.asarray([
            [1, 1, 0, 0, 3, 3],
            [1, 1, 0, 2, 3, 3],
    ]))

    gpu_input2 = cle.push(np.asarray([
            [0, 0, 1, 2, 2, 0],
            [0, 0, 1, 2, 2, 0],
    ]))

    gpu_reference = cle.push(np.asarray([

            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],

    ]))
    gpu_output = cle.subtract_labels(gpu_input1, gpu_input2)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
