import pyclesperanto_prototype as cle
import numpy as np

def test_generate_touch_matrix():
    
    gpu_input = cle.push_zyx(np.asarray([

            [1, 1, 0, 0, 0],
            [1, 1, 0, 3, 0],
            [0, 2, 2, 3, 0],
            [0, 2, 2, 0, 0],
            [0, 0, 0, 0, 4]

    ]))

    gpu_reference = cle.push_zyx(np.asarray([

            [0, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]

    ]).T)

    gpu_touch_matrix = cle.generate_touch_matrix(gpu_input)

    a = cle.pull_zyx(gpu_touch_matrix)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))













