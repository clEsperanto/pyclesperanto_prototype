import pyclesperanto_prototype as cle


import numpy as np

input1 = np.asarray([[1, 2, 3]])
input2 = np.asarray([[4, 5, 7]])


def test_squared_difference():
    reference = np.asarray([[9, 9, 16]])
    output = cle.squared_difference(input2, input1)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


