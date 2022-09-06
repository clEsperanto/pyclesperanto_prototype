def test_standard_deviation_of_n_most_touching_neighbors_map():
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

    reference = cle.replace_intensities(cle.asarray([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 2, 2, 0],
        [0, 1, 1, 1, 2, 2, 0],
        [0, 0, 3, 3, 3, 3, 0],
        [0, 0, 4, 4, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]), [0, 1, 1, 1, 3])

    result = cle.minimum_of_n_most_touching_neighbors_map(labels, labels, n=2)

    assert np.allclose(result, reference, 0.01)

