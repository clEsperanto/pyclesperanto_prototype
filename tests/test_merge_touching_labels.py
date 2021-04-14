import pyclesperanto_prototype as cle
import numpy as np

def test_merge_touching_labels():

    gpu_input = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 0],
            [0, 2, 2, 0, 3],
            [0, 0, 2, 0, 3],
        ]
    ]))
    gpu_output = cle.create_like(gpu_input)

    gpu_reference = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 2],
            [0, 0, 1, 0, 2],
        ]
    ]))



    cle.merge_touching_labels(gpu_input, gpu_output)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_merge_touching_labels2():

    gpu_input = cle.push(np.asarray([

        [1, 1, 0, 2, 0, 3, 0, 0, 0, 0],
        [1, 1, 2, 2, 0, 3, 0, 0, 4, 5],
        [1, 0, 0, 2, 0, 0, 0, 0, 4, 5],
        [7, 7, 7, 7, 7, 7, 7, 7, 7, 6],

    ]))
    gpu_output = cle.create_like(gpu_input)

    gpu_reference = cle.push(np.asarray([

        [2, 2, 0, 2, 0, 1, 0, 0, 0, 0],
        [2, 2, 2, 2, 0, 1, 0, 0, 2, 2],
        [2, 0, 0, 2, 0, 0, 0, 0, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],

    ]))



    cle.merge_touching_labels(gpu_input, gpu_output)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))