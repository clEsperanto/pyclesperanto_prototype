import pyclesperanto_prototype as cle
import numpy as np

def test_crop():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 1],
        [0, 0, 3, 1],
        [0, 0, 3, 1],
        [1, 1, 1, 1]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0],
        [0, 0, 3],
        [0, 0, 3]
    ]))

    result = cle.create(reference)
    cle.crop(test1, result, 0, 0)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    assert (np.array_equal(a, b))
