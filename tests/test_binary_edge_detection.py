import pyclesperanto_prototype as cle
import numpy as np

def test_binary_edge_detection():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]))

    test2 = cle.create(test1)
    cle.binary_edge_detection(test1, test2)

    print(test2)
    a = cle.pull_zyx(test2)
    assert (np.min(a) == 0)
    assert (np.max(a) == 1)
    assert (np.mean(a) - 12 / 36 < 0.001)


