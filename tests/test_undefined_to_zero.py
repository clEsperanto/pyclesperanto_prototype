import pyclesperanto_prototype as cle
import numpy as np


def test_undefined_to_zero():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    test2 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    divided = cle.divide_images(test1, test2)

    divided_no_nan = cle.undefined_to_zero(divided)

    print(divided)
    print(divided_no_nan)


    a = cle.pull(divided_no_nan)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

