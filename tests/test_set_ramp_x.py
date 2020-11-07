import pyclesperanto_prototype as cle
import numpy as np

def test_set_ramp_x():
    result = cle.push(np.asarray([
        [
            [0, 0, 0],
            [3, 4, 3],
            [3, 4, 3]
        ], [
            [3, 4, 3],
            [3, 4, 3],
            [3, 4, 3]
        ]
    ]))

    reference = cle.push(np.asarray([
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ], [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
    ]))

    cle.set_ramp_x(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.allclose(a, b, 0.001))
