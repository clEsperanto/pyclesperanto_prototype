def test_mode_of_touch_portion_within_range_neighbors_map():
    import numpy as np
    import pyclesperanto_prototype as cle

    intensities = cle.push(np.asarray([
        [0, 0, 1, 5],
        [0, 1, 1, 1],
        [0, 4, 1, 0],
        [0, 0, 0, 0]
    ]))

    labels = cle.push(np.asarray([
        [0, 0, 2, 5],
        [0, 3, 1, 2],
        [0, 4, 3, 0],
        [0, 0, 0, 0],
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    ))  # not sure if this is deterministically always those values... let's see over time

    result = cle.mode_of_touch_portion_within_range_neighbors_map(intensities, labels, minimum_touch_portion=0.09)

    print(result)
    print(reference)

    assert np.allclose(result, reference, 0.01)

