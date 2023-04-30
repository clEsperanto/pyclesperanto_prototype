import pyclesperanto_prototype as cle
import numpy as np

test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
    ], [
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
    ], [
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
    ]
]))

reference = cle.push(np.asarray([
    [4, 3, 3],
    [3, 4, 4],
    [4, 4, 3],
    [3, 3, 4]
]))

def test_x_position_of_maximum_x_projection():

    result = cle.create(reference)
    cle.x_position_of_maximum_x_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))


def test_x_position_of_maximum_x_projection_creator():
    result = cle.x_position_of_maximum_x_projection(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

def test_x_position_of_maximum_x_projection_creator_passing_none():
    result = cle.x_position_of_maximum_x_projection(test1, None)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))
