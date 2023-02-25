def test_generate_average_intensity_between_points_matrix():
    import pyclesperanto_prototype as cle
    import numpy as np

    image = np.zeros((10, 10))
    image[5:, :5] = 5
    image[5:, 5:] = 10

    coords = np.asarray([
        [1, 1],  # first point
        [8, 1],  # second ...
        [1, 8],
        [8, 8]
    ]).T

    touch_matrix = cle.generate_distance_matrix(coords, coords) > 0

    average_intensity_matrix = cle.generate_mean_intensity_between_points_matrix(image, coords, touch_matrix)

    reference = np.asarray([
        [0.,  0.,  0.,  0.,  0.],
        [0.,  0.,  0.,  2.5, 5.],
        [0.,  0.,  0.,  2.5, 5.],
        [0.,  2.5, 2.5, 0.,  7.5],
        [0.,  5.,  5.,  7.5, 0.]])

    assert cle.array_equal(reference, average_intensity_matrix)