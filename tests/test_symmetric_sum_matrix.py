import pyclesperanto_prototype as cle
import numpy as np

def test_symmetric_sum_matrix():
    
    gpu_input = cle.push(np.asarray([

            [0, 1, 0, 0, 0],
            [1, 0, 2, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0]

    ]))

    gpu_reference = cle.push(np.asarray([

        [0, 2,   0,   0, 0],
        [2, 0,   3,   1, 0],
        [0, 3,   0,   1, 0],
        [0, 1,   1,   0, 0],
        [0, 0,   0,   0, 0]

    ]))

    gpu_touch_matrix = cle.symmetric_sum_matrix(gpu_input)

    a = cle.pull(gpu_touch_matrix)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))













