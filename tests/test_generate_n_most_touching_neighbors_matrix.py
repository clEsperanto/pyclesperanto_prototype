def test_generate_n_most_touching_neighbors_matrix():
    import numpy as np
    import pyclesperanto_prototype as cle
    labels = cle.asarray([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 2, 2, 0],
        [0, 1, 1, 1, 2, 2, 0],
        [0, 0, 3, 3, 3, 3, 0],
        [0, 0, 4, 4, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ])
    labels = cle.scale(labels, factor_x=10, factor_y=10, auto_size=True).astype(np.uint32)

    reference = cle.asarray([
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 1., 1., 0., 0.],
        [0., 0., 0., 1., 0.],
    ])

    touch_count_matrix = cle.generate_touch_count_matrix(labels)
    print(touch_count_matrix)

    result = cle.generate_n_most_touching_neighbors_matrix(touch_count_matrix, n=1)

    assert cle.array_equal(reference, result)

    touch_portion_matrix = cle.generate_touch_portion_matrix(labels)
    print(touch_portion_matrix)

    result = cle.generate_n_most_touching_neighbors_matrix(touch_portion_matrix, n=1)

    assert cle.array_equal(reference, result)

    reference = cle.asarray([
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0.],
        [0., 1., 1., 0., 0.],
        [0., 0., 0., 1., 0.],
    ])
    result = cle.generate_n_most_touching_neighbors_matrix(touch_portion_matrix, n=2)
    assert cle.array_equal(reference, result)