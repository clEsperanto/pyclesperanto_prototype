import pyclesperanto_prototype as cle
import numpy as np


def test_get_center_of_mass():

    test = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]))

    c = cle.get_center_of_mass(test)

    print(c)

    assert (np.array_equal(c, [2, 1, 0]))
    print("ok get_center_of_mass")


