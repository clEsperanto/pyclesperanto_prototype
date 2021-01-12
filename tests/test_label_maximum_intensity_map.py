import pyclesperanto_prototype as cle
import numpy as np

def test_label_maximum_intensity_map_2d():

    intensity = cle.push(np.asarray([
        [1, 1, 2],
        [4, 0, 0],
        [5, 3, 0]
    ]))

    labels = cle.push(np.asarray([
        [1, 1, 2],
        [1, 0, 0],
        [3, 3, 0]
    ]))

    reference = cle.push(np.asarray([
        [4, 4, 2],
        [4, 0, 0],
        [5, 5, 0]
    ]
    ))

    result = cle.label_maximum_intensity_map(intensity, labels)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_label_maximum_intensity_map_3d():


    intensity = cle.push(np.asarray([
        [
            [1, 1, 2],
        ],[
            [4, 0, 0],
        ], [
            [5, 3, 0]
        ]
    ]))

    labels = cle.push(np.asarray([
        [
            [1, 1, 2],
        ], [
            [1, 0, 0],
        ], [
            [3, 3, 0]
        ]
    ]))

    reference = cle.push(np.asarray([
        [
            [4, 4, 2],
        ], [
            [4, 0, 0],
        ], [
            [5, 5, 0]
        ]
    ]
    ))

    result = cle.label_maximum_intensity_map(intensity, labels)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))




