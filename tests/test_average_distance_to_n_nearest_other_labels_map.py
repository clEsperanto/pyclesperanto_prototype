import pyclesperanto_prototype as cle
import numpy as np

def test_average_distance_of_n_nearest_other_labels_map():
    cle.select_device("gfx")

    labels = cle.push(np.asarray([
                    [1, 0, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2]
    ]))

    other_labels = cle.push(np.asarray([
                    [0, 2, 0, 0, 0, 3],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 4],
                    [0, 0, 0, 0, 5, 0]
    ]))


    reference = cle.push(np.asarray([
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1]
    ]))

    average_distance_to_n_nearest_other_labels_map = cle.average_distance_to_n_nearest_other_labels_map(labels, other_labels, n=1)

    a = cle.pull(average_distance_to_n_nearest_other_labels_map)
    b = cle.pull(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
