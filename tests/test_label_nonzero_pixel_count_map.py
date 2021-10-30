import pyclesperanto_prototype as cle
import numpy as np

def test_label_nonzero_pixel_count_map():
    labels1 = np.asarray([[1, 2, 2, 3]])
    labels2 = np.asarray([[1, 2, 0, 0]])

    reference12 = np.asarray([[1, 1, 1, 0]])
    reference21 = np.asarray([[1, 1, 0, 0]])

    result = cle.label_nonzero_pixel_count_map(labels1, labels2)
    assert (np.array_equal(result, reference12))

    result = cle.label_nonzero_pixel_count_map(labels2, labels1)
    assert (np.array_equal(result, reference21))