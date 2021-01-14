import pyclesperanto_prototype as cle
import numpy as np

def test_masked_voronoi_labeling():
    
    gpu_input = cle.push(np.asarray([
        [
            [1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
    ]))

    gpu_mask = cle.push(np.asarray([
        [
            [1, 1, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [1, 1, 1, 1, 0, 3],
            [1, 0, 0, 1, 0, 3],
            [1, 0, 1, 1, 0, 3],
            [2, 0, 1, 1, 0, 4],
            [2, 0, 0, 0, 0, 4],
            [2, 2, 2, 4, 4, 4],
        ]
    ]))

    gpu_output = cle.masked_voronoi_labeling(gpu_input, gpu_mask)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))