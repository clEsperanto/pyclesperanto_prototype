import pyclesperanto_prototype as cle
import numpy as np

def test_minimum_of_masked_pixels_mini_x():
    np_input = np.asarray([[1, 2, 3, 4]])
    np_mask = np.asarray([[0, 1, 1, 0]])

    gpu_input = cle.push_zyx(np_input)
    gpu_mask = cle.push_zyx(np_mask)

    result = cle.minimum_of_masked_pixels(gpu_input, gpu_mask)
    print(result)
    assert (result == 1)

def test_minimum_of_masked_pixels_mini_y():
    np_input = np.asarray([[1], [2], [3], [4]])
    np_mask = np.asarray([[0], [1], [1], [0]])

    gpu_input = cle.push_zyx(np_input)
    gpu_mask = cle.push_zyx(np_mask)

    result = cle.minimum_of_masked_pixels(gpu_input, gpu_mask)
    print(result)
    assert (result == 1)

def test_minimum_of_masked_pixels():
    np_input = np.asarray([
        [
            [1, 2, 3, 10],
            [4, 5, 6, 11],
            [7, 8, 9, 12]
        ],
        [
            [1, 2, 3, 13],
            [4, 5, 6, 14],
            [7, 8, 9, 15]
        ]
    ])

    np_mask = np.asarray([
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0]
        ],
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
    ])

    gpu_input = cle.push_zyx(np_input)
    gpu_mask = cle.push_zyx(np_mask)

    result = cle.minimum_of_masked_pixels(gpu_input, gpu_mask)
    print(result)
    assert (result == 2)

    gpu_input = cle.push(np_input)
    gpu_mask = cle.push(np_mask)

    result = cle.minimum_of_masked_pixels(gpu_input, gpu_mask)
    print(result)
    assert (result == 2)
