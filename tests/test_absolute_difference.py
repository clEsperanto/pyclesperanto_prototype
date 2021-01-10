import pyclesperanto_prototype as cle


import numpy as np

input1 = np.asarray([[1, 5, 3]])
input2 = np.asarray([[4, 2, 7]])


def test_absolute_difference():
    reference = np.asarray([[3, 3, 4]])
    output = cle.absolute_difference(input2, input1)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


