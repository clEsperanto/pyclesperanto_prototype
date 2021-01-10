import pyclesperanto_prototype as cle
import numpy as np


def test_point_index_list_to_mesh():
    positions = cle.push(np.asarray([
        [1, 1, 4, 4],
        [1, 4, 4, 1]
    ]))

    index_list = cle.push(np.asarray([
        [2, 3, 4, 1],
        [3,-1,-1,-1]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]))

    result = cle.create_like(reference)

    result = cle.point_index_list_to_mesh(positions, index_list, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
