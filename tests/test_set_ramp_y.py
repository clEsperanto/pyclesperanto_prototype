import pyclesperanto_prototype as cle
import numpy as np


def test_set_ramp_y():
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
            [1, 1, 1],
            [2, 2, 2]
        ], [
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2]
        ]
    ]))

    cle.set_ramp_y(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.allclose(a, b, 0.001))
    print("ok set_ramp_y")
