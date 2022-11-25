import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_position():
    np_input = np.asarray([
        [
            [1, 1, 1, 1,]
            [1, 1, 2, 1,]
            [1, 1, 1, 1,]
        ],
            [[1, 1, 1, 1,]
            [1, 1, 1, 1,]
            [2, 1, 1, 1,]]
        ])

    reference = (0, 1, 2)
    gpu_input = cle.push(np_input)
    result = cle.maximum_position(gpu_input)

    assert (result == reference)
