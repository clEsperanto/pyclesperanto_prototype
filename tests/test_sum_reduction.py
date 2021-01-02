import pyclesperanto_prototype as cle
import numpy as np

source = np.asarray([[0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]])
reference_4 = np.asarray([[2, 2, 1, 0]])
reference_2 = np.asarray([[1, 1, 0, 2, 0, 1, 0]])

def sum_reduction(source, blocksize):
    flagged_indices = cle.push_zyx(source)
    max_label = source.shape[1] - 1

    block_sums = cle.create([1, int((int(max_label) + 1) / blocksize) + 1])
    cle.sum_reduction_x(flagged_indices, block_sums, blocksize)

    return cle.pull_zyx(block_sums)

def test_sum_reduction():

    result = sum_reduction(source, 4)
    print(result)
    print(reference_4)
    assert np.array_equal(result, reference_4)

    result = sum_reduction(source, 2)
    print(result)
    print(reference_2)
    assert np.array_equal(result, reference_2)