import pyclesperanto_prototype as cle
import numpy as np


def test_maximum_images():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 3, 3, 4, 0],
        [0, 4, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))
    test2 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 2, 1, 3, 0],
        [0, 2, 1, 3, 0],
        [0, 1, 1, 3, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 2, 2, 3, 0],
        [0, 3, 3, 4, 0],
        [0, 4, 4, 5, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.maximum_images(test1, test2, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert (np.array_equal(a, b))

def test_maximum_images_with_types():
    import numpy as np
    test1 = cle.push(np.asarray([
        [0, 3, 3, 4, 0],
    ]))
    test2 = np.asarray([
        [0, 2, 1, 3, 0],
    ])

    reference = cle.push(np.asarray([
        [0, 2, 1, 3, 0],
    ]))

    result1 = cle.maximum_images(test1.astype(int), test2.astype(int))
    result2 = cle.maximum_images(test1.astype(float), test2.astype(float))
    result3 = cle.maximum_images(test1.astype(int), test2.astype(float))
    result4 = cle.maximum_images(test1.astype(np.uint16), test2.astype(np.float32))
    result5 = cle.maximum_images(test1.astype(np.uint32), test2.astype(np.float32))

    assert np.array_equal(result1, reference)
    assert np.array_equal(result2, reference)
    assert np.array_equal(result3, reference)
    assert np.array_equal(result4, reference)
    assert np.array_equal(result5, reference)


