import pyclesperanto_prototype as cle
import numpy as np

def test_label_spots_2d():

    gpu_input = cle.push_zyx(np.asarray([

            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1]

    ]).T)

    gpu_reference = cle.push_zyx(np.asarray([

            [0, 0, 0, 0, 0],
            [0, 1, 0, 3, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 4]

    ]).T)

    gpu_output = cle.label_spots(gpu_input)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_label_spots_3d():

    gpu_input = cle.push_zyx(np.asarray([
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

    gpu_reference = cle.push_zyx(np.asarray([
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

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
