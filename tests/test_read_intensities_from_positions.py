import pyclesperanto_prototype as cle
import numpy as np

def test_read_intensities_from_positions():

    intensities = cle.push_zyx(np.asarray([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

    pointlist = cle.push_zyx(np.asarray([
        [0, 1, 0],
        [0, 2, 2]
    ]
    ))

    reference = cle.push_zyx(np.asarray([
        [1, 8, 7]
    ]
    ))

    result = cle.read_intensities_from_positions(pointlist, intensities)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
