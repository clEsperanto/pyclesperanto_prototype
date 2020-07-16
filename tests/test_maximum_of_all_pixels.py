import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_of_all_pixels():

    gpu_input = cle.push(np.asarray([
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ]))

    result = cle.maximum_of_all_pixels(gpu_input)
    print(result)
    assert(result == 9)