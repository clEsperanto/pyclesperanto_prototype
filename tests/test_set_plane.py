import pyclesperanto_prototype as cle
import numpy as np
import pytest
import pyopencl as cl

@pytest.mark.xfail('LINUX and CI', reason='INVALID_ARG_SIZE on CI', raises=cl.LogicError)
def test_set_plane():
    result = cle.push(np.asarray([
        [
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3]
        ], [
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3]
        ]
    ]))

    reference = cle.push(np.asarray([
        [
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3]
        ], [
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3],
            [3, 4, 3, 3, 3]
        ]
    ]))

    cle.set_plane(result, 1, 4)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.allclose(a, b, 0.001))
    print("ok set_plane")
