import pyclesperanto_prototype as cle
import numpy as np

def test_merge_labels_according_to_touch_matrix():
    gpu_input = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 0],
            [0, 2, 2, 0, 3],
            [0, 0, 2, 0, 3],
        ]
    ]))

    touch_matrix = cle.push([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ])

    gpu_reference = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 0],
            [0, 2, 2, 0, 2],
            [0, 0, 2, 0, 2],
        ]
    ]))

    gpu_output = cle.merge_labels_according_to_touch_matrix(gpu_input, touch_matrix)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_merge_labels_according_to_touch_matrix2():
    gpu_input = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 0],
            [0, 2, 2, 0, 3],
            [0, 0, 2, 0, 3],
        ]
    ]))

    touch_matrix = cle.push([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ])

    gpu_reference = cle.push(np.asarray([
        [
            [1, 1, 0, 0, 0],
            [0, 2, 2, 0, 2],
            [0, 0, 2, 0, 2],
        ]
    ]))

    gpu_output = cle.merge_labels_according_to_touch_matrix(gpu_input, touch_matrix)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
