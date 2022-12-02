import pyclesperanto_prototype as cle
import numpy as np

def test_standard_deviation_touch_portion():

    labels = cle.push(np.asarray([
        [1, 1, 3, 3, 3, 3],
        [1, 1, 3, 3, 3, 3],
        [1, 1, 3, 3, 3, 3],
        [2, 2, 2, 4, 4, 4],
        [2, 2, 2, 4, 4, 5],
        [2, 2, 2, 4, 5, 5],
    ]))

    reference = cle.push([[ 0, 0.10000001, 0.11111111, 0.12698412, 0.04444444, 0.]])


    std_touch_portion = cle.standard_deviation_touch_portion(labels)

    print(std_touch_portion)

    assert np.allclose(std_touch_portion, reference, 0.001)
