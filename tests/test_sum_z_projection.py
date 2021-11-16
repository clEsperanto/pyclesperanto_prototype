import pyclesperanto_prototype as cle
import numpy as np

def test_sum_z_projection():
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
        [ 2.,  6.,  0., 24., 18.],
         [ 5.,  6.,  1., 15., 28.],
         [ 9.,  8.,  3., 14., 30.],
         [ 4., 10.,  1., 22., 19.],
         [25.,  0., 30.,  0., 50.]
    ]))

    result = cle.create(reference)
    cle.sum_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)
    print(a)

    assert (np.allclose(a, b, 0.01))

def test_sum_z_projection2():
    test1 = cle.push(np.asarray([
        [
            [1, 0],
        ], [
            [0, 2],
        ], [
            [0, 2],
        ], [
            [0, 2],
        ], [
            [1, 0],
        ]
    ]))

    reference = cle.push(np.asarray([
        [2, 6]
    ]))

    result = cle.sum_z_projection(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)
    print(a)

    assert (np.allclose(a, b, 0.01))
