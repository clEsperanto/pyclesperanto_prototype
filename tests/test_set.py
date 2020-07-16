import pyclesperanto_prototype as cle
import numpy as np


def test_set():
    result = cle.create((5, 5))

    reference = cle.push(np.asarray([
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3]
    ]))

    cle.set(result, 3)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.allclose(a, b, 0.001))
    print("ok set")