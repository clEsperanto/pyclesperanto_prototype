import pyclesperanto_prototype as cle
import numpy as np


def test_draw_box():
    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 2, 2, 2, 0],
        [0, 2, 2, 2, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create((5, 5))
    cle.set(result, 0)
    cle.draw_box(result, 1, 1, 0, 2, 1, 1, 2)

    print(result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    assert (np.array_equal(a, b))
