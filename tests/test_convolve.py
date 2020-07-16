import pyclesperanto_prototype as cle
import numpy as np

def test_convolve():

    test = cle.push(np.asarray([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))

    test1 = cle.push(np.asarray([
        [0, 1, 0],
        [1, 2, 1],
        [0, 1, 0]
    ]))

    test2 = cle.create(test)
    cle.convolve(test, test1, test2)

    print(test2)

    a = cle.pull(test1)
    b = cle.pull(test2)
    assert (np.min(a) == np.min(b))
    assert (np.max(a) == np.max(b))
    assert (np.mean(a) == np.mean(b))
    print ("ok convolve")