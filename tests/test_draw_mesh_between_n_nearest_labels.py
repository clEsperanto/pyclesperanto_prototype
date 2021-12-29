import pyclesperanto_prototype as cle
import numpy as np

def test_draw_mesh_between_n_nearest_labels():

    labels = cle.push(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [0, 0, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0, 2],
                    [0, 0, 0, 0, 0, 2],
                    [0, 0, 0, 0, 0, 2]
    ]))

    reference = cle.push(np.asarray([
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]
    ]))


    distance_mesh_between_n_nearest_labels = cle.draw_mesh_between_n_closest_labels(labels, n=1)

    a = cle.pull(distance_mesh_between_n_nearest_labels)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
