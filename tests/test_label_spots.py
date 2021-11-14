import pyclesperanto_prototype as cle
import numpy as np

def test_label_spots_2d():

    gpu_input = cle.push(np.asarray([

            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1]

    ]))

    gpu_reference = cle.push(np.asarray([

            [0, 0, 0, 0, 0],
            [0, 1, 0, 2, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0],
            [0, 0, 0, 0, 4]

    ]))

    gpu_output = cle.label_spots(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(b)
    print(a)

    assert (np.array_equal(a, b))

def test_label_spots_3d():

    gpu_input = cle.push(np.asarray([
        [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]
        ],[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0]
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 2, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0]
        ],[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 4],
            [5, 0, 0, 0, 0]
        ]
    ]))

    gpu_output = cle.label_spots(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
