import pyclesperanto_prototype as cle
import numpy as np

def test_mean_x_projection():

    test1 = cle.push_zyx(np.asarray([
        [
            [1, 0, 0, 0, 9],
            [0, 2, 0, 8, 0],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [5, 0, 6, 0, 10]
        ],[
            [0, 2, 0, 8, 0],
            [1, 0, 0, 0, 9],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [5, 0, 6, 0, 10]
        ],[
            [0, 2, 0, 8, 0],
            [3, 0, 1, 0, 10],
            [0, 4, 0, 7, 0],
            [1, 0, 0, 0, 9],
            [5, 0, 6, 0, 10]
        ],[
            [0, 2, 0, 8, 0],
            [1, 0, 0, 0, 9],
            [0, 4, 0, 7, 0],
            [3, 0, 1, 0, 10],
            [5, 0, 6, 0, 10]
        ],[
            [1, 0, 0, 0, 9],
            [0, 4, 0, 7, 0],
            [3, 0, 1, 0, 10],
            [0, 2, 0, 8, 0],
            [5, 0, 6, 0, 10]
        ]
    ]).T)

    reference = cle.push_zyx(np.asarray([
        [0.4, 1.0, 1.8, 0.8, 5.],
        [1.2, 1.2, 1.6, 2.0, 0.],
        [0.,  0.2, 0.6, 0.2, 6.],
        [4.8, 3.0, 2.8, 4.4, 0.],
        [3.6, 5.6, 6.0, 3.8, 10.]
    ]).T)

    result = cle.create(reference)
    cle.mean_x_projection(test1, result)


    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))

