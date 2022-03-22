import pyclesperanto_prototype as cle
import numpy as np

def test_reduce_labels_to_label_edges():
    test = np.asarray([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0,0,0,0, 1,1,1,0],
        [0,0,2,0, 1,1,1,0],
        [0,0,0,0, 1,1,1,0],
        [0,3,3,3, 4,4,4,0],
        [0,3,3,3, 4,4,4,0],
        [0,3,3,3, 4,4,4,0],
        [0,0,0,0, 0,0,0,0],
    ])

    reference = np.asarray([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0,0,0,0, 1,1,1,0],
        [0,0,2,0, 1,0,1,0],
        [0,0,0,0, 1,1,1,0],
        [0,3,3,3, 4,4,4,0],
        [0,3,0,3, 4,0,4,0],
        [0,3,3,3, 4,4,4,0],
        [0,0,0,0, 0,0,0,0]
    ])

    result = cle.reduce_labels_to_label_edges(test)

    print(result)
    print(reference)

    assert np.allclose(reference, result)



