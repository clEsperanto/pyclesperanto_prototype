import pyclesperanto_prototype as cle
import numpy as np

def test_prefix_in_x():
    test = cle.push(np.asarray([
        [1, 3, 4],
        [1, 5, 6]
    ]))

    reference0 = cle.push(np.asarray([
        [0, 1, 3, 4],
        [0, 1, 5, 6]
    ]))

    reference2 = cle.push(np.asarray([
        [2, 1, 3, 4],
        [2, 1, 5, 6]
    ]))

    result0 = cle.prefix_in_x(test)
    result2 = cle.prefix_in_x(test, scalar=2)

    assert np.array_equal(result0, reference0)
    assert np.array_equal(result2, reference2)
