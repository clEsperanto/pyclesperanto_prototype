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
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0]
]))

def test_y_position_of_minimum_y_projection():

    result = cle.create(reference)
    cle.y_position_of_minimum_y_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))


def test_y_position_of_minimum_y_projection_creator():
    result = cle.y_position_of_minimum_y_projection(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

def test_y_position_of_minimum_y_projection_creator_passing_none():
    result = cle.y_position_of_minimum_y_projection(test1, None)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))
