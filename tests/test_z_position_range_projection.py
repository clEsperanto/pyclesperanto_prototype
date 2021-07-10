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
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [9, 8, 8, 8, 9],
        [8, 9, 10, 9, 7],
        [10, 10, 7, 7, 10],
        [7, 7, 9, 10, 8],
        [10, 10, 10, 10, 10]
    ],[
        [9, 0, 0, 0, 9],
        [0, 9, 10, 9, 0],
        [10, 10, 0, 0, 10],
        [0, 0, 9, 10, 0],
        [10, 10, 10, 10, 10]
    ],
]))

def test_z_position_range_projection():


    temp = cle.create_2d_xy(reference)
    cle.z_position_of_maximum_z_projection(test1, temp)

    result = cle.create(reference)
    cle.z_position_range_projection(test1, temp, result, start_z=-1, end_z=1)


    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))


def test_z_position_range_projection_creator():
    temp = cle.z_position_of_maximum_z_projection(test1)
    result = cle.z_position_range_projection(test1, temp, start_z=-1, end_z=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

def test_z_position_range_projection_creator_passing_none():
    temp = cle.z_position_of_maximum_z_projection(test1, None)
    result = cle.z_position_range_projection(test1, temp, start_z=-1, end_z=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))

