import pyclesperanto_prototype as cle
import numpy as np


def test_draw_line():
    reference = cle.push(np.asarray([
        [2, 2, 0, 0, 0],
        [2, 2, 2, 0, 0],
        [0, 2, 2, 2, 0],
        [0, 0, 2, 2, 2],
        [0, 0, 0, 2, 2]
    ]))

    result = cle.create((5, 5))
    cle.set(result, 0)
    cle.draw_line(result, 1, 1, 0, 4, 4, 0, 1, 2)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    assert (np.array_equal(a, b))
