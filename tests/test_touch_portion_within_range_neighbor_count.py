import pyclesperanto_prototype as cle
import numpy as np

def test_touch_portion_within_range_neighbor_count():

    labels = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 2, 2, 0],
        [0, 1, 1, 1, 2, 2, 0],
        [0, 0, 3, 3, 3, 3, 0],
        [0, 0, 4, 4, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]))

    reference = cle.push(np.asarray([[0, 2, 2, 3, 1]]))
    result = cle.touch_portion_within_range_neighbor_count(labels)
    print(reference)
    print(result)
    assert np.array_equal(reference, result)

    reference = cle.push(np.asarray([[0, 1, 1, 3, 1]]))
    result = cle.touch_portion_within_range_neighbor_count(labels, minimum_touch_portion=0.15)
    print(reference)
    print(result)
    assert np.array_equal(reference, result)


    reference = cle.push(np.asarray([[0, 0, 0, 1, 1]]))
    result = cle.touch_portion_within_range_neighbor_count(labels, minimum_touch_portion=0.25)
    print(reference)
    print(result)
    assert np.array_equal(reference, result)
