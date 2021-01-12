import pyclesperanto_prototype as cle
import numpy as np

def test_set_nonzero_pixels_to_pixelindex():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 1],
        [0, 0, 3, 1],
        [0, 0, 3, 1],
        [1, 1, 1, 1]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 13],
        [0, 0, 10, 14],
        [0, 0, 11, 15],
        [4, 8, 12, 16]
    ]))

    result = cle.create(test1)
    cle.set_non_zero_pixels_to_pixel_index(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert (np.array_equal(a, b))
