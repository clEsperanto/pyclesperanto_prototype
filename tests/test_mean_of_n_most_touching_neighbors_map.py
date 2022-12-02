def test_mean_of_n_most_touching_neighbors_map():
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
    ]), [0, 2, 2, 2.5, 3.5])

    result = cle.mean_of_n_most_touching_neighbors_map(labels, labels, n=3)

    print(result)

    assert np.allclose(result, reference, 0.01)

