import pyclesperanto_prototype as cle
import numpy as np

def test_combine_labels_2d():

    gpu_input1 = cle.push(np.asarray([
            [1, 1, 0, 0, 3, 3],
            [1, 1, 0, 2, 3, 3],
    ]))

    gpu_input2 = cle.push(np.asarray([
            [0, 1, 1, 2, 2, 0],
            [0, 1, 1, 2, 2, 0],
    ]))

    gpu_reference = cle.push(np.asarray([

            [1, 3, 3, 4, 4, 2],
            [1, 3, 3, 4, 4, 2],

    ]))
    gpu_output = cle.combine_labels(gpu_input1, gpu_input2)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
