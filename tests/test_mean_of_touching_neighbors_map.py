import pyclesperanto_prototype as cle
import numpy as np

def test_mean_of_touching_neighbors_map():

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
        [2.333, 2.333, 3, 3],
        [2.333, 0, 0, 3],
        [3.666, 0, 0, 4],
        [3.666, 3.666, 4, 4]
    ]
    ))

    result = cle.mean_of_touching_neighbors_map(intensities, labels)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))
