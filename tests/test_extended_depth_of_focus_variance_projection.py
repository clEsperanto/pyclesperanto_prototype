import pyclesperanto_prototype as cle
import numpy as np

test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ], [
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ], [
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ], [
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ], [
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]).T)

reference = cle.push(np.asarray([
    [9, 0, 0, 0, 9],
    [0, 9, 10, 9, 0],
    [10, 10, 0, 0, 10],
    [0, 0, 9, 10, 0],
    [10, 10, 10, 10, 10]
]))

def test_extended_depth_of_focus_variance_projection_projection():
    result = cle.create(reference)
    cle.extended_depth_of_focus_variance_projection(test1, result, radius_x=1, radius_y=1, sigma=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_extended_depth_of_focus_variance_projection_creator():
    result = cle.extended_depth_of_focus_variance_projection(test1, radius_x=1, radius_y=1, sigma=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

def test_extended_depth_of_focus_variance_projection_creator_passing_none():
    result = cle.extended_depth_of_focus_variance_projection(test1, None, radius_x=1, radius_y=1, sigma=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

