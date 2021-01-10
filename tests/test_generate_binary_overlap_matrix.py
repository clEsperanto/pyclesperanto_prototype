import pyclesperanto_prototype as cle
import numpy as np

def test_generate_binary_overlap_matrix_2d():
    
    gpu_input1 = cle.push(np.asarray([

            [1, 1, 0, 0, 0],
            [1, 1, 0, 3, 0],
            [0, 2, 2, 3, 0],
            [0, 2, 2, 0, 0],
            [0, 0, 0, 0, 4]

    ]))

    gpu_input2 = cle.push(np.asarray([

            [1, 1, 2, 2, 2],
            [1, 1, 2, 2, 2],
            [1, 0, 0, 2, 2],
            [1, 0, 0, 2, 2],
            [1, 2, 2, 2, 2]

    ]))


    gpu_reference = cle.push(np.asarray([

            [0, 1, 1],
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1],
            [0, 0, 1]

    ]).T)

    gpu_binary_overlap_matrix = cle.generate_binary_overlap_matrix(gpu_input1, gpu_input2)

    a = cle.pull(gpu_binary_overlap_matrix)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.01))


def test_generate_binary_overlap_matrix_3d():
    gpu_input1 = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 3, 0],
        ],[
            [0, 2, 2, 0, 0],
            [0, 0, 0, 0, 4]
        ]
    ]))

    gpu_input2 = cle.push(np.asarray([
        [
            [1, 1, 2, 2, 2],
            [1, 1, 2, 2, 2],
        ],[
            [1, 0, 0, 2, 2],
            [1, 2, 2, 2, 2]
        ]
    ]))

    gpu_reference = cle.push(np.asarray([

        [0, 1, 1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 0, 1]

    ]).T)

    gpu_binary_overlap_matrix = cle.generate_binary_overlap_matrix(gpu_input1, gpu_input2)

    a = cle.pull(gpu_binary_overlap_matrix)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.01))









