import pyclesperanto_prototype as cle
import numpy as np

def test_label_label_maximum_extension_ratio_map_2d():

    labels = cle.push_zyx(np.asarray([
        [1, 1, 2],
        [1, 0, 2],
        [3, 3, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [1.1396203, 1.1396203, 1],
        [1.1396203, 0, 1],
        [1, 1, 0]
    ]
    ))

    result = cle.label_maximum_extension_ratio_map(labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))


def test_label_label_maximum_extension_ratio_map_3d():

    labels = cle.push_zyx(np.asarray([
        [
            [1, 1, 2],
        ], [
            [1, 0, 2],
        ], [
            [3, 3, 0]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        [
            [1.1396203, 1.1396203, 1],
        ], [
            [1.1396203, 0, 1],
        ], [
            [1, 1, 0]
        ]
    ]
    ))

    result = cle.label_maximum_extension_ratio_map(labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))




