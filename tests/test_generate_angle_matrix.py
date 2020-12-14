import pyclesperanto_prototype as cle
import numpy as np

def test_generate_angle_matrix():

    input = cle.push_zyx(np.asarray([

            [5, 0, 4, 0, 3],
            [0, 6, 0, 0, 0],
            [7, 0, 1, 0, 2],
            [0, 0, 0, 0, 0],
            [8, 0, 9, 0, 0]
    ]))

    reference = cle.push(np.asarray([
            [0., -45.,  90.,  45.,  45.,   0., -45., -90.]
    ]))



    pointlist = cle.labelled_spots_to_pointlist(input)
    angle_matrix = cle.generate_angle_matrix(pointlist, pointlist)

    angle_matrix_degrees = cle.radians_to_degrees(angle_matrix)

    angle_from_1 = cle.crop(angle_matrix_degrees, start_x=2, start_y=1, width=8, height=1)

    a = cle.pull_zyx(angle_from_1)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))
