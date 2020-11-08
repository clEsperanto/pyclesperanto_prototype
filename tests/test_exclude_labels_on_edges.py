import pyclesperanto_prototype as cle
import numpy as np

def test_exclude_labels_on_edges_2d():
    
    gpu_input = cle.push(np.asarray([

            [0, 0, 2, 0, 0, 0, 0],
            [0, 1, 2, 0, 7, 0, 0],
            [0, 1, 0, 0, 7, 5, 5],
            [8, 8, 8, 0, 0, 0, 0],
            [0, 4, 4, 0, 3, 0, 0],
            [0, 4, 4, 6, 0, 0, 0],

    ]))

    gpu_reference = cle.push(np.asarray([

            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 3, 0, 0],
            [0, 1, 0, 0, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],

    ]))

    gpu_output = cle.exclude_labels_on_edges(gpu_input)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_exclude_labels_on_edges_3d():
    gpu_input = cle.push(np.asarray([
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],[
            [0, 0, 2, 0, 0, 0, 0],
            [0, 1, 2, 0, 7, 0, 0],
            [0, 1, 0, 0, 7, 5, 5],
            [8, 8, 8, 0, 0, 0, 0],
            [0, 4, 4, 9, 3, 0, 0],
            [0, 4, 4, 6, 0, 0, 0],
        ],[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ]))

    gpu_output = cle.exclude_labels_on_edges(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))