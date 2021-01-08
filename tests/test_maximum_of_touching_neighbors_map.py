import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_of_touching_neighbors_map():

    intensities = cle.push_zyx(np.asarray([
        [1, 1, 2, 2],
        [1, 0, 0, 2],
        [4, 0, 0, 6],
        [4, 4, 6, 6]
    ]))

    labels = cle.push_zyx(np.asarray([
        [1, 1, 2, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, 3, 4, 4],
    ]))

    reference = cle.push_zyx(np.asarray([
        [3, 3, 6, 6],
        [3, 0, 0, 6],
        [6, 0, 0, 6],
        [6, 6, 6, 6]
    ]
    ))

    result = cle.maximum_of_touching_neighbors_map(intensities, labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))
