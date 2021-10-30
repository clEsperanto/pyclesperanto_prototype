import pyclesperanto_prototype as cle
import numpy as np

def test_label_overlap_count_map():
    labels1 = np.asarray([[1, 2, 2, 3]])
    labels2 = np.asarray([[1, 2, 3, 4]])

    reference12 = np.asarray([[1, 2, 2, 1]])
    reference21 = np.asarray([[1, 1, 1, 1]])

    result = cle.label_overlap_count_map(labels1, labels2)
    assert (np.array_equal(result, reference12))

    result = cle.label_overlap_count_map(labels2, labels1)
    assert (np.array_equal(result, reference21))