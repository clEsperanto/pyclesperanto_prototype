import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_y_projection():
    test1 = cle.push(np.asarray([
        [
            [1, 0, 0, 0, 9],
            [0, 2, 0, 8, 0],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [5, 0, 6, 0, 10]
        ], [
            [0, 2, 0, 8, 0],
            [1, 0, 0, 0, 9],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [5, 0, 6, 0, 10]
        ], [
            [0, 2, 0, 8, 0],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [1, 0, 0, 0, 9],
            [5, 0, 6, 0, 10]
        ], [
            [0, 2, 0, 8, 0],
            [1, 0, 0, 0, 9],
            [0, 4, 0, 7, 0],
            [3, 0, 1, 0, 10],
            [5, 0, 6, 0, 10]
        ], [
            [1, 0, 0, 0, 9],
            [0, 4, 0, 7, 0],
            [3, 0, 1, 0, 10],
            [0, 2, 0, 8, 0],
            [5, 0, 6, 0, 10]
        ]
    ]))

    reference = cle.push(np.asarray([
        [5, 4, 6, 8, 10],
        [5, 4, 6, 8, 10],
        [5, 4, 6, 8, 10],
        [5, 4, 6, 8, 10],
        [5, 4, 6, 8, 10]
    ]))

    result = cle.create(reference)
    cle.maximum_y_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

def test_maximum_y_projection2():
    test1 = cle.push(np.asarray(
        [
            [1, 0, 0, 0, 9],
            [0, 2, 0, 8, 0],
            [3, 0, 1, 0, 10],
        ]))

    reference = cle.push(np.asarray([
        [3, 2, 1, 8, 10]
    ]))

    result = cle.maximum_y_projection(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

def test_maximum_y_projection_against_numpy():
    from skimage.data import camera
    image = camera()

    max_cle = cle.maximum_y_projection(image)
    max_np = image.max(axis=0)

    print(max_cle.get()[0])
    print(max_np)

    assert np.array_equal(max_cle.get()[0], max_np)

def test_maximum_y_projection_against_numpy_small():
    from skimage.data import camera
    image = camera()[0:2, 0:10]

    max_cle = cle.maximum_y_projection(image)
    max_np = image.max(axis=0)

    print(max_cle.get()[0])
    print(max_np)

    assert np.array_equal(max_cle.get()[0], max_np)

