import pyclesperanto_prototype as cle
import numpy as np

def test_touch_matrix_to_mesh():

    gpu_touch_matrix = cle.push(np.asarray([
                    [0, 0, 0],
                    [0, 0, 1],
                    [0, 0, 0]
    ]))

    gpu_point_list = cle.push(np.asarray([
                    [1, 2],
                    [4, 5]
    ]))

    gpu_output = cle.create([5, 5])
    cle.set(gpu_output, 0)

    gpu_reference = cle.push(np.asarray([
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0]
    ]))



    cle.touch_matrix_to_mesh(gpu_point_list, gpu_touch_matrix, gpu_output)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)


    assert (np.array_equal(a, b))
