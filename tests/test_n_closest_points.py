

import numpy as np
import pyclesperanto_prototype as cle

def test_n_closest_points():

    labels = cle.push(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2]
    ]))

    reference = cle.push(np.asarray(
                    [[0, 3, 3, 1]]
    ))

    centroids = cle.centroids_of_labels(labels)
    distance_matrix = cle.generate_distance_matrix(centroids, centroids)

    max_float = np.finfo(np.float).max

    cle.set_where_x_equals_y(distance_matrix, max_float)
    cle.set_row(distance_matrix, 0, max_float)
    cle.set_column(distance_matrix, 0, max_float)

    n_closest_points = cle.n_closest_points(distance_matrix, n=1, ignore_background=False)

    a = cle.pull(n_closest_points)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))



import numpy as np
import pyclesperanto_prototype as cle

def test_n_closest_points_ignore_background():

    labels = cle.push(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2]
    ]))

    reference = cle.push(np.asarray(
                    [[3, 3, 1]]
    ))

    centroids = cle.centroids_of_labels(labels)
    distance_matrix = cle.generate_distance_matrix(centroids, centroids)

    max_float = np.finfo(np.float).max

    cle.set_where_x_equals_y(distance_matrix, max_float)
    cle.set_row(distance_matrix, 0, max_float)
    cle.set_column(distance_matrix, 0, max_float)

    n_closest_points = cle.n_closest_points(distance_matrix, n=1)

    a = cle.pull(n_closest_points)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))

