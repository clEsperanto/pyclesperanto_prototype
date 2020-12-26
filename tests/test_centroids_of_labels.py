import pyclesperanto_prototype as cle
import numpy as np

def test_centroids_of_labels():

    labels = cle.push_zyx(np.asarray([
        [1, 1, 2],
        [1, 2, 2],
        [3, 3, 3]
    ]))

    reference = cle.push_zyx(np.asarray([
        #     CENTROID_X(25),
        [0.33333334,    1.6666666,    1.],
        #     CENTROID_Y(26),
        [0.33333334,  0.6666667,   2.]
    ]
    ))

    result = cle.centroids_of_labels(labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_centroids_of_labels_3d():

    labels = cle.push_zyx(np.asarray([
        [
            [1, 1, 2],
        ], [
            [1, 2, 2],
        ], [
            [3, 3, 3]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        #     CENTROID_X(25),
        [0.5,    1.6666666,    1.],
        #     CENTROID_Y(26),
        [0.,    0.,    0.],
        #     CENTROID_Z(27),
        [0.5,  0.6666667,   2.],
    ]
    ))

    result = cle.centroids_of_labels(labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))




