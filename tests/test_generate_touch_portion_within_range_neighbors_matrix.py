def test_generate_touch_portion_within_range_neighbor_matrix():
    import numpy as np
    import pyclesperanto_prototype as cle

    labels = cle.asarray([
        [
            [0, 1, 1, 2, 2, 3],
            [0, 1, 1, 2, 2, 3]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
    ])

    reference = cle.asarray([
        # 0  1  2  3
        [0,    1, 1, 1],  # 0
        [1, 0,   0, 0],    # 1
        [0, 0, 0,   1],  # 2
        [0, 0,   0, 0],    # 3
    ])

    touch_portion_matrix = cle.generate_touch_portion_matrix(labels)

    result = cle.generate_touch_portion_within_range_neighbors_matrix(touch_portion_matrix, minimum_touch_portion=0.4)

    print(reference)
    print(result)

    assert cle.array_equal(result, reference)
