import pyclesperanto_prototype as cle
import numpy as np
import pyopencl as cl

def test_watershed():


    altitude = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 2, 2, 2, 1, 1, 1, 0],
        [0, 1, 3, 2, 2, 2, 1, 2, 3, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))
    seeds = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))
    mask = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))
    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 2, 2, 2, 0],
        [0, 1, 1, 1, 1, 1, 2, 2, 2, 0],
        [0, 1, 1, 1, 1, 1, 0, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))

    result = cle.watershed(altitude, seeds, mask)

    print(reference)
    print(result)

    assert np.array_equal(reference, result)

if __name__ == "__main__":
    test_watershed()
