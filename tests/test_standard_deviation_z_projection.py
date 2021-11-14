import pyclesperanto_prototype as cle
import numpy as np

def test_standard_deviation_z_projection():
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
        [0.55, 1.10, 0, 4.38, 4.93],
        [1.22, 1.79, 0.45, 4.12, 5.13],
        [1.64, 2.19, 0.55, 3.83, 5.48],
        [1.30, 2, 0.45, 4.03, 5.22],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(reference)
    cle.standard_deviation_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.allclose(a, b, 0.01))
