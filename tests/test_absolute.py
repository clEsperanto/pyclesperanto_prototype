import pyclesperanto_prototype as cle
import numpy as np

def test_absolute():
    test = cle.push(np.asarray([
        [1, -1],
        [1, -1]
    ]))

    test2 = cle.create(test)
    cle.absolute(test, test2)

    print(test2)

    a = cle.pull(test2)
    assert (np.min(a) == 1)
    assert (np.max(a) == 1)
    assert (np.mean(a) == 1)
    print ("ok absolute")
