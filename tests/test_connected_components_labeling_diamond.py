import pyclesperanto_prototype as cle
import numpy as np

def test_connected_components_labeling_diamond():
    
    gpu_input = cle.push(np.asarray([
        [
            [0, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 0, 0, 1]
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [0, 1, 0, 2],
            [0, 1, 0, 0],
            [3, 0, 0, 4]
        ]
    ]))

    gpu_output = cle.connected_components_labeling_diamond(gpu_input)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))