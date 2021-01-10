import pyclesperanto_prototype as cle
import numpy as np

def test_labelled_spots_to_pointlist():

    gpu_input = cle.push_zyx(np.asarray([

            [0, 0, 0, 0, 0],
            [0, 1, 0, 3, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 4]

    ]).T)

    gpu_reference = cle.push_zyx(np.asarray([

            [1, 1],
            [3, 2],
            [1, 3],
            [4, 4]

    ]).T)



    gpu_output = cle.labelled_spots_to_pointlist(gpu_input)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
