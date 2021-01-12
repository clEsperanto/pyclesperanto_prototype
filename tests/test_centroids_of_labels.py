import pyclesperanto_prototype as cle
import numpy as np

def test_centroids_of_labels():

    labels = cle.push(np.asarray([
        [1, 1, 2],
        [1, 2, 2],
        [3, 3, 3]
    ]))

    reference = cle.push(np.asarray([
        #     CENTROID_X(25),
        [0.33333334,    1.6666666,    1.],
        #     CENTROID_Y(26),
        [0.33333334,  0.6666667,   2.]
    ]
    ))

    result = cle.centroids_of_labels(labels)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.0001))


def test_centroids_of_labels_3d():

    labels = cle.push(np.asarray([
        [
            [1, 1, 2],
        ], [
            [1, 2, 2],
        ], [
            [3, 3, 3]
        ]
    ]))

    reference = cle.push(np.asarray([
        #     CENTROID_X(25),
        [0.33333334,    1.6666666,    1.],
        #     CENTROID_Y(26),
        [0.,    0.,    0.],
        #     CENTROID_Z(27),
        [0.33333334,  0.6666667,   2.],
    ]
    ))

    result = cle.centroids_of_labels(labels)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.0001))



