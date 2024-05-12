import pyclesperanto_prototype as cle
import numpy as np


def test_stitch_horizontally_linear_blending_overlap0():
    test1 = cle.push(np.asarray([
        [1, 1],
        [1, 1]
    ]))
    test2 = cle.push(np.asarray([
        [2, 2, 2],
        [2, 2, 2]
    ]))

    reference = cle.push(np.asarray([
        [1, 1, 2, 2, 2],
        [1, 1, 2, 2, 2]
    ]))

    result = cle.stitch_horizontally_linear_blending(test1, test2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.01))

def test_stitch_horizontally_linear_blending_overlap1():
    test1 = cle.push(np.asarray([
        [1, 1],
        [1, 1]
    ]))
    test2 = cle.push(np.asarray([
        [2, 2, 2],
        [2, 2, 2]
    ]))

    reference = cle.push(np.asarray([
        [1, 1.5, 2, 2],
        [1, 1.5, 2, 2]
    ]))

    result = cle.stitch_horizontally_linear_blending(test1, test2, num_pixels_overlap=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.01))


def test_stitch_horizontally_linear_blending_overlap2():
    test1 = cle.push(np.asarray([
        [1, 1, 1],
        [1, 1, 1]
    ]))
    test2 = cle.push(np.asarray([
        [2, 2, 2],
        [2, 2, 2]
    ]))

    reference = cle.push(np.asarray([
        [1, 1.33, 1.67, 2],
        [1, 1.33, 1.67, 2]
    ]))

    result = cle.stitch_horizontally_linear_blending(test1, test2, num_pixels_overlap=2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.01))

