import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_of_proximal_neighbors_map():

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
        [4, 4, 6, 6],
        [4, 0, 0, 6],
        [6, 0, 0, 6],
        [6, 6, 6, 6]
    ]
    ))

    result = cle.maximum_of_proximal_neighbors_map(intensities, labels, max_distance=3)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))
