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
        [3.94, 3.46, 4.21, 3.19, 4.27],
        [3.46, 3.94, 4.21, 3.19, 4.27],
        [3.46, 4.21, 3.19, 3.94, 4.27],
        [3.46, 3.94, 3.19, 4.21, 4.27],
        [3.94, 3.19, 4.21, 3.46, 4.27]
    ]))

    result = cle.create(reference)
    cle.standard_deviation_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.allclose(a, b, 0.01))
    print("ok standard_deviation_z_projection")
