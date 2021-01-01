import pyclesperanto_prototype as cle
import numpy as np

def test_euclidean_distance_from_label_centroid_map():

    labels = cle.push_zyx(np.asarray([
        [1, 1, 1, 2],
        [1, 1, 1, 2],
        [1, 1, 1, 2],
        [2, 2, 2, 2]
    ]))

    reference = cle.push_zyx(np.asarray([
        [1.4142135, 1, 1.4142135, 2.3079278],
        [1, 0, 1, 1.4285713],
        [1.4142135, 1, 1.4142135, 0.86896616],
        [2.3079278, 1.4285713, 0.86896616, 1.2121831]
    ]
    ))
    print(cle.centroids_of_background_and_labels(labels))

    result = cle.euclidean_distance_from_label_centroid_map(labels)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))
