import pyclesperanto_prototype as cle
import numpy as np

def test_label_pixel_count_map():

    labels = cle.push(np.asarray([
        [1, 1, 2],
        [1, 0, 0],
        [3, 3, 0]
    ]))

    reference = cle.push(np.asarray([
        [3, 3, 1],
        [3, 0, 0],
        [2, 2, 0]
    ]
    ))

    result = cle.label_pixel_count_map(labels)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_label_pixel_count_map_3d():

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
            [3, 3, 1],
        ], [
            [3, 0, 0],
        ], [
            [2, 2, 0]
        ]
    ]
    ))

    result = cle.label_pixel_count_map(labels)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))




