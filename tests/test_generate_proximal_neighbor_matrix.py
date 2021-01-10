import pyclesperanto_prototype as cle
import numpy as np


def test_generate_proximal_neighbors_matrix():
    positions = cle.push_zyx(np.asarray([
        [1, 1, 4, 4],
        [1, 4, 4, 1]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]))

    result = cle.create_like(reference)

    distance_matrix = cle.generate_distance_matrix(positions, positions)

    n_nearest_neighbor_matrix = cle.generate_proximal_neighbors_matrix(distance_matrix, min_distance=3, max_distance=3)

    result = cle.touch_matrix_to_mesh(positions, n_nearest_neighbor_matrix, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))



def test_generate_distal_neighbors_matrix():
    positions = cle.push_zyx(np.asarray([
        [1, 1, 5, 5],
        [1, 5, 5, 1]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
    ]))

    result = cle.create_like(reference)

    distance_matrix = cle.generate_distance_matrix(positions, positions)

    n_nearest_neighbor_matrix = cle.generate_proximal_neighbors_matrix(distance_matrix, min_distance=4.1)

    result = cle.touch_matrix_to_mesh(positions, n_nearest_neighbor_matrix, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
