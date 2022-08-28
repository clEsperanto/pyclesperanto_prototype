def test_generate_touch_count_matrix():
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
        [0, 6, 4, 2],  # 0
        [6, 0, 2, 0],  # 1
        [4, 2, 0, 2],  # 2
        [2, 0, 2, 0],  # 3
    ])

    result = cle.generate_touch_count_matrix(labels)

    assert cle.array_equal(result, reference)
