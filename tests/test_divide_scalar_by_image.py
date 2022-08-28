import pyclesperanto_prototype as cle
import numpy as np


def test_divide_scalar_by_image():
    test1 = cle.push(np.asarray([
        [5, 5],
        [1, 1],
        [2, 2]
    ]))

    reference = cle.push(np.asarray([
        [2, 2],
        [10, 10],
        [5, 5]
    ]))

    result = cle.create(test1)
    cle.divide_scalar_by_image(test1, result, 10)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))
