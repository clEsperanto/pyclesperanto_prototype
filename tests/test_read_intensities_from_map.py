import pyclesperanto_prototype as cle
import numpy as np

def test_read_intensities_from_map():

    intensities = cle.push(np.asarray([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

    labels = cle.push(np.asarray([
        [8, 0, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]))

    reference = cle.push(np.asarray([
        [2, 9, 8, 7, 6, 5, 4, 3, 1]
    ]
    ))

    result = cle.read_intensities_from_map(labels, intensities)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
