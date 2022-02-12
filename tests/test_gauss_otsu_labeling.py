import pyclesperanto_prototype as cle
import numpy as np

def test_gauss_otsu_labeling():
    
    gpu_input = cle.push(np.asarray([

            [0, 0, 1, 1, 0, 0],
            [0, 1, 8, 9, 1, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 1, 8, 7, 1],
            [0, 0, 1, 1, 1, 0],

    ]))


    gpu_reference = cle.push(np.asarray([

            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 0],
            [0, 0, 2, 2, 2, 2],
            [0, 0, 2, 2, 2, 0],

    ]))

    gpu_output = cle.gauss_otsu_labeling(gpu_input, outline_sigma=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
