import pyclesperanto_prototype as cle
import numpy as np

def test_set_ramp_z():
    result = cle.push_zyx(np.asarray([
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

    reference = cle.push_zyx(np.asarray([
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

    cle.set_ramp_z(result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)

    assert (np.allclose(a, b, 0.001))
