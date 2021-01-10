import pyclesperanto_prototype as cle
import numpy as np


def test_generate_n_nearest_neighbors_matrix():
    positions = cle.push(np.asarray([
        [1, 1, 4, 4],
        [1, 4, 4, 1]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]))

    result = cle.create_like(reference)

    distance_matrix = cle.generate_distance_matrix(positions, positions)

    n_nearest_neighbor_matrix = cle.generate_n_nearest_neighbors_matrix(distance_matrix, n=2)

    result = cle.touch_matrix_to_mesh(positions, n_nearest_neighbor_matrix, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
