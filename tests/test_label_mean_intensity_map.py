import pyclesperanto_prototype as cle
import numpy as np

def test_label_mean_intensity_map_2d():

    intensity = cle.push_zyx(np.asarray([
        [1, 1, 2],
        [4, 0, 0],
        [5, 3, 0]
    ]))

    labels = cle.push_zyx(np.asarray([
        [1, 1, 2],
        [1, 0, 0],
        [3, 3, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [2, 2, 2],
        [2, 0, 0],
        [4, 4, 0]
    ]
    ))

    result = cle.label_mean_intensity_map(intensity, labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_label_mean_intensity_map_3d():


    intensity = cle.push_zyx(np.asarray([
        [
            [1, 1, 2],
        ],[
            [4, 0, 0],
        ], [
            [5, 3, 0]
        ]
    ]))

    labels = cle.push_zyx(np.asarray([
        [
            [1, 1, 2],
        ], [
            [1, 0, 0],
        ], [
            [3, 3, 0]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        [
            [2, 2, 2],
        ], [
            [2, 0, 0],
        ], [
            [4, 4, 0]
        ]
    ]
    ))

    result = cle.label_mean_intensity_map(intensity, labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))




