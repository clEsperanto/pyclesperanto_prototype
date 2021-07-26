import pyclesperanto_prototype as cle
import numpy as np

def test_relabel_sequential():

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



    cle.relabel_sequential(gpu_input, gpu_output)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))