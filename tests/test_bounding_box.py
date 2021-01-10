import pyclesperanto_prototype as cle
import numpy as np

def test_bounding_box_2d():

    test = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    bb = cle.bounding_box(test)
    print(bb)

    assert bb[1] == 1
    assert bb[0] == 1

    assert bb[4] == 2
    assert bb[3] == 2

def test_bounding_box_3d():

    test = cle.push_zyx(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]]))

    bb = cle.bounding_box(test)
    print(bb)

    assert bb[2] == 0
    assert bb[1] == 1
    assert bb[0] == 1

    assert bb[5] == 1
    assert bb[4] == 2
    assert bb[3] == 2
