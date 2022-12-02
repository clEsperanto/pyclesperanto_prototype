def test_generate_touch_portion_matrix():
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
        [0,    6/8, 4/8, 2/4],  # 0
        [6/12, 0,   2/8, 0],    # 1
        [4/12, 2/8, 0,   2/4],  # 2
        [2/12, 0,   2/8, 0],    # 3
    ])

    result = cle.generate_touch_portion_matrix(labels)

    print(reference)
    print(result)

    assert cle.array_equal(result, reference)
