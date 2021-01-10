import pyclesperanto_prototype as cle
import numpy as np

def test_detect_label_edges():

    test = cle.push(np.asarray([
        [1, 1, 2, 2, 2],
        [1, 1, 2, 2, 2],
        [3, 3, 3, 2, 2],
        [3, 3, 3, 2, 0],
        [3, 3, 3, 0, 0]
    ]))

    result = cle.create(test)
    cle.detect_label_edges(test, result)

    reference = cle.push(np.asarray([
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0]
    ]))

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)

    assert (np.array_equal(a, b))

