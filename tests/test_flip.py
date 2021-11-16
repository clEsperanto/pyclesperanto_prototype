import pyclesperanto_prototype as cle
import numpy as np

def test_flip():
    test = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 1, 3, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 2, 1, 0],
        [0, 0, 2, 1, 0],
        [0, 0, 3, 1, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test)
    cle.flip(test, result, True, False, False)

    print(reference.get())
    print(result.get())

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.array_equal(a, b))

