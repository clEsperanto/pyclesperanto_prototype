import pyclesperanto_prototype as cle
import numpy as np

def test_object_splitting_otsu_labeling():
    
    gpu_input = cle.push(np.asarray([

            [0, 0, 5, 5, 0, 0],
            [0, 5, 8, 9, 1, 0],
            [0, 5, 7, 6, 1, 1],
            [0, 0, 0, 5, 5, 1],
            [0, 0, 0, 5, 5, 1],
            [0, 0, 5, 5, 5, 1],
            [0, 0, 5, 5, 5, 0],

    ]))


    gpu_reference = cle.push(np.asarray([

            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 2, 2, 0],
            [0, 0, 2, 2, 2, 0],
            [0, 0, 2, 2, 2, 0],

    ]))

    gpu_output = cle.eroded_otsu_labeling(gpu_input, number_of_erosions=1, outline_sigma=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
