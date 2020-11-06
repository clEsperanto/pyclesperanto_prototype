import pyclesperanto_prototype as cle
import numpy as np

def test_close_index_gaps_in_label_maps():

    gpu_input = cle.push(np.asarray([
        [
            [1, 2, 3],
            [1, 6, 6],
            [7, 8, 9]
        ]
    ]))
    gpu_output = cle.create_like(gpu_input)

    gpu_reference = cle.push(np.asarray([
        [
            [1, 2, 3],
            [1, 4, 4],
            [5, 6, 7]
        ]
    ]))



    cle.close_index_gaps_in_label_map(gpu_input, gpu_output)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))