import pyclesperanto_prototype as cle
import numpy as np


def test_draw_sphere():
    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 2, 2, 2, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create((5, 5))
    cle.set(result, 0)
    cle.draw_sphere(result, 2, 2, 0, 1, 1, 0, 2)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    assert (np.array_equal(a, b))
    print("ok draw_sphere")
