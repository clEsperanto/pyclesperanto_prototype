import pyclesperanto_prototype as cle
import numpy as np


def test_set_image_borders():
    result = cle.push(np.asarray([
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3]
    ]))

    reference = cle.push(np.asarray([
        [4, 4, 4, 4, 4],
        [4, 3, 3, 3, 4],
        [4, 3, 3, 3, 4],
        [4, 3, 3, 3, 4],
        [4, 4, 4, 4, 4]
    ]))

    cle.set_image_borders(result, 4)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.allclose(a, b, 0.001))
