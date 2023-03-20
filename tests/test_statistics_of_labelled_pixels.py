import pyclesperanto_prototype as cle
import numpy as np


def test_statistics_of_labelled_pixels():
    intensity = cle.push(np.asarray([
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4]
    ]))

    labels = cle.push(np.asarray([
        [1, 1, 2],
        [1, 2, 2],
        [3, 3, 3]
    ]))

    reference = cle.push(np.asarray([
        #IDENTIFIER(0),
        [1.,          2.,          3.],
        # BOUNDING_BOX_X(1),
        [0.,          1.,          0.],
        #     BOUNDING_BOX_Y(2),
        [0.,    0.,    2.],
        #     BOUNDING_BOX_Z(3),
        [0.,          0.,          0.],

        #     BOUNDING_BOX_END_X(4),
        [1.,    2.,    2.],
        #     BOUNDING_BOX_END_Y(5),
        [1.,    1.,    2.],
        #     BOUNDING_BOX_END_Z(6),
        [0.,    0.,    0.],

        #     BOUNDING_BOX_WIDTH(7),
        [2.,    2.,    3.],
        #     BOUNDING_BOX_HEIGHT(8),
        [2.,    2.,    1.],
        #     BOUNDING_BOX_DEPTH(9),
        [1.,          1.,          1.],

        #     MINIMUM_INTENSITY(10),
        [0.,    2.,    2.],
        #     MAXIMUM_INTENSITY(11),
        [1.,          3.,          4.],
        #     MEAN_INTENSITY(12)
        [0.6666667,    2.3333333,    3.],
        #     SUM_INTENSITY(13),
        [2.,          7.,          9.],

        #     STANDARD_DEVIATION_INTENSITY(14),
        [0.47140452, 0.4714045, 0.8164966],
        #     PIXEL_COUNT(15),
        [3.,    3.,    3.],
        #     SUM_INTENSITY_TIMES_X(16),
        [1.,         12.,         11. ],
        #     SUM_INTENSITY_TIMES_Y(17),
        [1.,          5.,         18. ],
        #     SUM_INTENSITY_TIMES_Z(18),
        [0.,          0.,          0.],
        #     MASS_CENTER_X(19),
        [0.5,    1.7142857,    1.2222222],
        #     MASS_CENTER_Y(20),
        [0.5,         0.71428573,  2.],
        #     MASS_CENTER_Z(21),
        [0.,    0.,    0.],
        #     SUM_X(22),
        [1.,          5.,          3. ],
        #     SUM_Y(23),
        [1.,          2.,          6. ],
        #     SUM_Z(24),
        [0.,          0.,          0.],
        #     CENTROID_X(25),
        [0.33333334,    1.6666666,    1.],
        #     CENTROID_Y(26),
        [0.33333334,  0.6666667,   2.],
        #     CENTROID_Z(27),
        [0.,    0.,    0.],
        #     SUM_DISTANCE_TO_MASS_CENTER(28),
        [2.1213202,   1.9426796,   2.2222223],
        #     MEAN_DISTANCE_TO_MASS_CENTER(29),
        [0.70710677,  0.6475599,   0.7407408],
        #     MAX_DISTANCE_TO_MASS_CENTER(30),
        [0.70710677,  0.7693094,   1.2222222],
        #     MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO(31),
        [1.,          1.1880127,   1.6499999],
        #     SUM_DISTANCE_TO_CENTROID(32),
        [1.9621165, 1.9621165, 2.],
        #     MEAN_DISTANCE_TO_CENTROID(33),
        [0.65403885, 0.65403885, 0.6666667],
        #     MAX_DISTANCE_TO_CENTROID(34),
        [0.74535596, 0.745356, 1.],
        #     MAX_MEAN_DISTANCE_TO_CENTROID_RATIO(35),
        [1.1396203, 1.1396204, 1.5],
        #     STANDARD_ERROR_INTENSITY(36);
        [0.27216553, 0.27216551, 0.4714043]
    ]
    ))

    result = cle.statistics_of_labelled_pixels(intensity, labels)

    print("bbox_min_x", result['bbox_min_x'])

    result_image = cle.push_regionprops(result, first_row_index=1)

    a = cle.pull(result_image)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.0001))

def test_statistics_of_labelled_pixels_3d():
    intensity = cle.push(np.asarray([
        [
            [0, 1, 2],
        ],[
            [1, 2, 3],
        ], [
            [2, 3, 4]
        ]
    ]))

    labels = cle.push(np.asarray([
        [
            [1, 1, 2],
        ], [
            [1, 2, 2],
        ], [
            [3, 3, 3]
        ]
    ]))

    reference = cle.push(np.asarray([
        # IDENTIFIER(0),
        [1., 2., 3.],
        # BOUNDING_BOX_X(1),
        [0., 1., 0.],
        #     BOUNDING_BOX_Y(2),
        [0., 0., 0.],
        #     BOUNDING_BOX_Z(3),
        [0., 0., 2.],

        #     BOUNDING_BOX_END_X(4),
        [1., 2., 2.],
        #     BOUNDING_BOX_END_Y(5),
        [0., 0., 0.],
        #     BOUNDING_BOX_END_Z(6),
        [1., 1., 2.],

        #     BOUNDING_BOX_WIDTH(7),
        [2., 2., 3.],
        #     BOUNDING_BOX_HEIGHT(8),
        [1., 1., 1.],
        #     BOUNDING_BOX_DEPTH(9),
        [2., 2., 1.],

        #     MINIMUM_INTENSITY(10),
        [0., 2., 2.],
        #     MAXIMUM_INTENSITY(11),
        [1., 3., 4.],
        #     MEAN_INTENSITY(12)
        [0.6666667, 2.3333333, 3.],
        #     SUM_INTENSITY(13),
        [2., 7., 9.],

        #     STANDARD_DEVIATION_INTENSITY(14),
        [0.47140452, 0.4714045, 0.8164966],
        #     PIXEL_COUNT(15),
        [3., 3., 3.],
        #     SUM_INTENSITY_TIMES_X(16),
        [1., 12., 11.],
        #     SUM_INTENSITY_TIMES_Y(17),
        [0., 0., 0.],
        #     SUM_INTENSITY_TIMES_Z(18),
        [1., 5., 18.],
        #     MASS_CENTER_X(19),
        [0.5, 1.7142857, 1.2222222],
        #     MASS_CENTER_Y(20),
        [0., 0., 0.],
        #     MASS_CENTER_Z(21),
        [0.5, 0.71428573, 2.],
        #     SUM_X(22),
        [1., 5., 3.],
        #     SUM_Y(23),
        [0., 0., 0.],
        #     SUM_Z(24),
        [1., 2., 6.],
        #     CENTROID_X(25),
        [0.33333334, 1.6666666, 1.],
        #     CENTROID_Y(26),
        [0., 0., 0.],
        #     CENTROID_Z(27),
        [0.33333334, 0.6666667, 2.],
        #     SUM_DISTANCE_TO_MASS_CENTER(28),
        [2.1213202, 1.9426795, 2.2222223],
        #     MEAN_DISTANCE_TO_MASS_CENTER(29),
        [0.70710677, 0.6475599, 0.7407408],
        #     MAX_DISTANCE_TO_MASS_CENTER(30),
        [0.70710677, 0.7693094, 1.2222222],
        #     MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO(31),
        [1., 1.1880127, 1.6499999],
        #     SUM_DISTANCE_TO_CENTROID(32),
        [1.9621165, 1.9621165, 2.],
        #     MEAN_DISTANCE_TO_CENTROID(33),
        [0.65403885, 0.65403885, 0.6666667],
        #     MAX_DISTANCE_TO_CENTROID(34),
        [0.74535596, 0.745356, 1.],
        #     MAX_MEAN_DISTANCE_TO_CENTROID_RATIO(35),
        [1.1396203, 1.1396204, 1.5],
        #     STANDARD_ERROR_INTENSITY(36);
        [0.27216553, 0.27216551, 0.4714043]
    ]
    ))

    result = cle.statistics_of_labelled_pixels(intensity, labels)

    print("\n")
    print("standard_deviation_intensity", result['standard_deviation_intensity'])

    result_image = cle.push_regionprops(result, first_row_index=1)

    a = cle.pull(result_image)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.0001))


def test_standard_deviation_and_standard_error():
    import numpy as np

    image = np.asarray([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    labels = np.asarray([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])

    print("numpy standard deviation", np.std(image))
    print("numpy variance", np.var(image))
    print("numpy standard error", np.std(image) / np.sqrt(image.size))

    stats = cle.statistics_of_labelled_pixels(image, labels)

    print("std", stats['standard_deviation_intensity'][0])
    print("sterr", stats['standard_error_intensity'][0])

    from numpy import testing
    testing.assert_almost_equal(stats['standard_deviation_intensity'][0], 2.58, decimal=1)
    testing.assert_almost_equal(stats['standard_error_intensity'][0], 0.86, decimal=1)

