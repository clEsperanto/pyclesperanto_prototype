import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_position():
    np_input= np.asarray([
            [
                [1, 2, 3, 10],
                [4, 16, 6, 11],
                [7, 8, 9, 12]
            ],
            [
                [1, 2, 3, 13],
                [4, 5, 6, 16],
                [7, 8, 9, 15]
            ]
        ])

    reference = (0, 1, 1)
    gpu_input = cle.push(np_input)
    result = cle.maximum_position(gpu_input)

    assert (result == reference)
