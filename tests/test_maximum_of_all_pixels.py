import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_of_all_pixels():
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

    gpu_input = cle.push_zyx(np_input)
    result = cle.maximum_of_all_pixels(gpu_input)
    print(result)
    assert (result == 15)

    gpu_input = cle.push_zyx(np_input)
    result = cle.maximum_of_all_pixels(gpu_input)
    print(result)
    assert (result == 15)
