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

    reference = cle.push([
        [0.10000001, 0.10000001, 0.12698412, 0.12698412, 0.12698412, 0.12698412],
        [0.10000001, 0.10000001, 0.12698412, 0.12698412, 0.12698412, 0.12698412],
        [0.10000001, 0.10000001, 0.12698412, 0.12698412, 0.12698412, 0.12698412],

        [0.11111111, 0.11111111, 0.11111111, 0.04444444, 0.04444444, 0.04444444],
        [0.11111111, 0.11111111, 0.11111111, 0.04444444, 0.04444444, 0],
        [0.11111111, 0.11111111, 0.11111111, 0.04444444, 0, 0],
    ])


    std_touch_portion = cle.standard_deviation_touch_portion_map(labels)

    print(std_touch_portion)

    assert cle.array_equal(std_touch_portion, reference)
