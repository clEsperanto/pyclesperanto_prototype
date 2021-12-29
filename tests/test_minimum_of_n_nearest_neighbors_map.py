import pyclesperanto_prototype as cle
import numpy as np

def test_minimum_of_n_nearest_neighbors_map():

    intensities = cle.push(np.asarray([
        [1, 1, 2, 2],
        [1, 0, 0, 2],
        [4, 0, 0, 6],
        [4, 4, 6, 6]
    ]))

    labels = cle.push(np.asarray([
        [1, 1, 2, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, 3, 4, 4],
    ]))

    reference = cle.push(np.asarray([
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 2],
        [1, 1, 2, 2]
    ]
    ))

    result = cle.minimum_of_n_nearest_neighbors_map(intensities, labels, n=2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))
