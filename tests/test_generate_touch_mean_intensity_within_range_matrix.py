import numpy as np
import pyclesperanto_prototype as cle

def test_generate_touch_mean_intensity_within_range_matrix():
    labels = cle.asarray([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0],
            [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0],
            [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0],
            [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])

    intensity = cle.asarray([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]) * 10

    reference = cle.asarray([
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ])

    result = cle.generate_touch_mean_intensity_within_range_matrix(intensity, labels, maximum_intensity=5)

    print(reference)
    print(result)

    assert np.array_equal(reference, result)
