import pyclesperanto_prototype as cle
import numpy as np

def test_set_column():
    result = cle.push(np.asarray([
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3]
    ]))

    reference = cle.push(np.asarray([
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
        [3, 3, 3, 3, 3]
    ]))

    cle.set_column(result, 3, 4)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.allclose(a, b, 0.001))
    print("ok set_column")
