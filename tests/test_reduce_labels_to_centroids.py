import pyclesperanto_prototype as cle
import numpy as np

def test_reduce_labels_to_centroids():
    test = np.asarray([
        [0,0,0, 1,1,1],
        [0,2,0, 1,1,1],
        [0,0,0, 1,1,1],
        [3,3,3, 4,4,4],
        [3,3,3, 4,4,4],
        [3,3,3, 4,4,4],
    ])

    reference = np.asarray([
        [0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0],
    ])

    result = cle.reduce_labels_to_centroids(test)

    print(result)
    print(reference)

    assert np.allclose(reference, result)



