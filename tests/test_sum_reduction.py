import pyclesperanto_prototype as cle
import numpy as np

source = np.asarray([[0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]])
reference_4 = np.asarray([[2, 2, 1]])
reference_2 = np.asarray([[1, 1, 0, 2, 0, 1]])

def sum_reduction(source, blocksize):
    flagged_indices = cle.push(source)

    block_sums = cle.sum_reduction_x(flagged_indices, blocksize=blocksize)

    return cle.pull(block_sums)

def test_sum_reduction():

    result = sum_reduction(source, 4)
    print(result)
    print(reference_4)
    assert np.array_equal(result, reference_4)

    result = sum_reduction(source, 2)
    print(result)
    print(reference_2)
    assert np.array_equal(result, reference_2)