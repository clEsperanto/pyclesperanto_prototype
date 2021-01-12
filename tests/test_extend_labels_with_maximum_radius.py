import pyclesperanto_prototype as cle
import numpy as np

def test_extend_labels_with_maximum_radius_2d():
    
    gpu_input = cle.push(np.asarray([

            [1, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 3],

    ]))

    gpu_reference = cle.push(np.asarray([

            [1, 1, 0, 0, 2, 2],
            [1, 1, 0, 0, 2, 2],
            [0, 0, 4, 4, 4, 0],
            [0, 0, 4, 4, 4, 0],
            [5, 5, 4, 4, 4, 3],
            [5, 5, 0, 0, 3, 3],

    ]))

    gpu_output = cle.extend_labels_with_maximum_radius(gpu_input, radius=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_extend_labels_with_maximum_radius_3d():
    gpu_input = cle.push(np.asarray([
        [
            [0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 3],
        ], [
            [1, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0],
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 2, 2],
            [1, 1, 0, 0, 2, 2],
            [0, 0, 4, 4, 4, 0],
            [0, 0, 4, 4, 4, 0],
            [5, 5, 4, 4, 4, 3],
            [5, 5, 0, 0, 3, 3],
        ],[
            [1, 1, 0, 0, 2, 2],
            [1, 1, 0, 0, 2, 2],
            [0, 0, 4, 4, 4, 0],
            [0, 0, 4, 4, 4, 0],
            [5, 5, 4, 4, 4, 3],
            [5, 5, 0, 0, 3, 3],
        ]
    ]))

    gpu_output = cle.extend_labels_with_maximum_radius(gpu_input, radius=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))