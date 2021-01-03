import pyclesperanto_prototype as cle
import numpy as np

def test_statistics_of_background_and_labelled_pixels():
    intensity = cle.push_zyx(np.asarray([
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4]
    ]))

    labels = cle.push_zyx(np.asarray([
        [0, 0, 1],
        [0, 1, 1],
        [2, 2, 2]
    ]))

    reference = cle.push_zyx(np.asarray([
        #IDENTIFIER(0),
        [0.,          1.,          2.],
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
        [0.,          0.,          0.],# Todo; not supported yet
        #     SUM_INTENSITY_TIMES_Y(17),
        [0.,    0.,    0.],# Todo; not supported yet
        #     SUM_INTENSITY_TIMES_Z(18),
        [0.,          0.,          0.],# Todo; not supported yet
        #     MASS_CENTER_X(19),
        [0.5,    1.7142857,    1.2222222],
        #     MASS_CENTER_Y(20),
        [0.5,         0.71428573,  2.],
        #     MASS_CENTER_Z(21),
        [0.,    0.,    0.],
        #     SUM_X(22),
        [0.,          0.,          0.],# Todo; not supported yet
        #     SUM_Y(23),
        [0.,     0.,    0.],# Todo; not supported yet
        #     SUM_Z(24),
        [0.,          0.,          0.],# Todo; not supported yet
        #     CENTROID_X(25),
        [0.33333334,    1.6666666,    1.],
        #     CENTROID_Y(26),
        [0.33333334,  0.6666667,   2.],
        #     CENTROID_Z(27),
        [0.,    0.,    0.],
        #     SUM_DISTANCE_TO_MASS_CENTER(28),
        [0.,          0.,          0.],# Todo; not supported yet
        #     MEAN_DISTANCE_TO_MASS_CENTER(29),
        [0.,    0.,    0.],# Todo; not supported yet
        #     MAX_DISTANCE_TO_MASS_CENTER(30),
        [0.,          0.,          0.],# Todo; not supported yet
        #     MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO(31),
        [0.,    0.,    0.],# Todo; not supported yet
        #     SUM_DISTANCE_TO_CENTROID(32),
        [1.9621165, 1.9621165, 2.],
        #     MEAN_DISTANCE_TO_CENTROID(33),
        [0.65403885, 0.65403885, 0.6666667],
        #     MAX_DISTANCE_TO_CENTROID(34),
        [0.74535596, 0.745356, 1.],
        #     MAX_MEAN_DISTANCE_TO_CENTROID_RATIO(35);
        [1.1396203, 1.1396204, 1.5]
    ]
    ))

    result = cle.statistics_of_background_and_labelled_pixels(intensity, labels, use_gpu=False)
    result_image = cle.push_regionprops(result, first_row_index=0)

    a = cle.pull_zyx(result_image)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.0001))


def test_statistics_of_background_and_labelled_pixels_3d():
    intensity = cle.push_zyx(np.asarray([
        [
            [0, 1, 2],
        ],[
            [1, 2, 3],
        ], [
            [2, 3, 4]
        ]
    ]))

    labels = cle.push_zyx(np.asarray([
        [
            [0, 0, 1],
        ], [
            [0, 1, 1],
        ], [
            [2, 2, 2]
        ]
    ]))

    reference = cle.push_zyx(np.asarray([
        #IDENTIFIER(0),
        [0.,         1.,          2.],
        # BOUNDING_BOX_X(1),
        [0.,          1.,          0.],
        #     BOUNDING_BOX_Y(2),
        [0.,          0.,          0.],
        #     BOUNDING_BOX_Z(3),
        [0., 0., 2.],

        #     BOUNDING_BOX_END_X(4),
        [1.,    2.,    2.],
        #     BOUNDING_BOX_END_Y(5),
        [0.,    0.,    0.],
        #     BOUNDING_BOX_END_Z(6),
        [1., 1., 2.],

        #     BOUNDING_BOX_WIDTH(7),
        [2.,         2.,          3.],
        #     BOUNDING_BOX_HEIGHT(8),
        [1.,         1.,          1.],
        #     BOUNDING_BOX_DEPTH(9),
        [2., 2., 1.],

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
        [0.,          0.,          0.],# Todo; not supported yet
        #     SUM_INTENSITY_TIMES_Y(17),
        [0.,    0.,    0.],# Todo; not supported yet
        #     SUM_INTENSITY_TIMES_Z(18),
        [0.,          0.,          0.],# Todo; not supported yet
        #     MASS_CENTER_X(19),
        [0.5,    1.7142857,    1.2222222],
        #     MASS_CENTER_Y(20),
        [0.,    0.,    0.],
        #     MASS_CENTER_Z(21),
        [0.5,         0.71428573,  2.],
        #     SUM_X(22),
        [0.,          0.,          0.],# Todo; not supported yet
        #     SUM_Y(23),
        [0.,     0.,    0.],# Todo; not supported yet
        #     SUM_Z(24),
        [0.,          0.,          0.],# Todo; not supported yet
        #     CENTROID_X(25),
        [0.33333334,    1.6666666,    1.],
        #     CENTROID_Y(26),
        [0.,    0.,    0.],
        #     CENTROID_Z(27),
        [0.33333334,  0.6666667,   2.],
        #     SUM_DISTANCE_TO_MASS_CENTER(28),
        [0.,          0.,          0.],# Todo; not supported yet
        #     MEAN_DISTANCE_TO_MASS_CENTER(29),
        [0.,    0.,    0.],# Todo; not supported yet
        #     MAX_DISTANCE_TO_MASS_CENTER(30),
        [0.,          0.,          0.],# Todo; not supported yet
        #     MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO(31),
        [0.,    0.,    0.],# Todo; not supported yet
        #     SUM_DISTANCE_TO_CENTROID(32),
        [1.9621165, 1.9621165, 2.],
        #     MEAN_DISTANCE_TO_CENTROID(33),
        [0.65403885, 0.65403885, 0.6666667],
        #     MAX_DISTANCE_TO_CENTROID(34),
        [0.74535596, 0.745356, 1.],
        #     MAX_MEAN_DISTANCE_TO_CENTROID_RATIO(35);
        [1.1396203, 1.1396204, 1.5]
    ]
    ))

    result = cle.statistics_of_background_and_labelled_pixels(intensity, labels, use_gpu=False)
    result_image = cle.push_regionprops(result, first_row_index=0)

    a = cle.pull_zyx(result_image)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.0001))


def test_statistics_of_background_and_labelled_pixels_compare_to_clij2():
    from skimage.io import imread

    blobs = cle.push_zyx(imread('data/mini_blobs.tif'))
    labels = cle.push_zyx(imread('data/mini_blobs_otsu_labels_excluded_edges_imagej.tif'))

    regionprops = cle.statistics_of_background_and_labelled_pixels(blobs, labels, use_gpu=False)
    table = cle.pull_zyx(cle.transpose_xy(cle.push_regionprops(regionprops)))


    print(table)

    import numpy as np
    # np.savetxt('../data/mini_blobs_measurements_pyclesperanto.csv', table,delimiter=',')
    clij_reference_table = np.loadtxt('data/mini_blobs_measurements_clij.csv', delimiter=',', skiprows=1)
    # chop off first column as ImageJ saved an additional counter column
    clij_reference_table = clij_reference_table[:, 1:]

    print(clij_reference_table)

    columns_to_test = [
        cle.STATISTICS_ENTRY.IDENTIFIER.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_X.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_Y.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_Z.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_END_X.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_END_Y.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_END_Z.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_WIDTH.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_HEIGHT.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_DEPTH.value,
        cle.STATISTICS_ENTRY.MINIMUM_INTENSITY.value,
        cle.STATISTICS_ENTRY.MAXIMUM_INTENSITY.value,
        cle.STATISTICS_ENTRY.MEAN_INTENSITY.value,
        cle.STATISTICS_ENTRY.SUM_INTENSITY.value,
        cle.STATISTICS_ENTRY.STANDARD_DEVIATION_INTENSITY.value,
        cle.STATISTICS_ENTRY.PIXEL_COUNT.value,
        cle.STATISTICS_ENTRY.MASS_CENTER_X.value,
        cle.STATISTICS_ENTRY.MASS_CENTER_Y.value,
        cle.STATISTICS_ENTRY.MASS_CENTER_Z.value,
        cle.STATISTICS_ENTRY.CENTROID_X.value,
        cle.STATISTICS_ENTRY.CENTROID_Y.value,
        cle.STATISTICS_ENTRY.CENTROID_Z.value,
        # Errors:
        cle.STATISTICS_ENTRY.SUM_DISTANCE_TO_CENTROID.value,
        cle.STATISTICS_ENTRY.MEAN_DISTANCE_TO_CENTROID.value,
        cle.STATISTICS_ENTRY.MAX_DISTANCE_TO_CENTROID.value,
        cle.STATISTICS_ENTRY.MAX_MEAN_DISTANCE_TO_CENTROID_RATIO.value
    ]

    # TODO: not yet implemented:
    not_yet_implemeneted_columns = [
        cle.STATISTICS_ENTRY.SUM_INTENSITY_TIMES_X.value,
        cle.STATISTICS_ENTRY.SUM_INTENSITY_TIMES_Y.value,
        cle.STATISTICS_ENTRY.SUM_INTENSITY_TIMES_Z.value,
        cle.STATISTICS_ENTRY.SUM_X.value,
        cle.STATISTICS_ENTRY.SUM_Y.value,
        cle.STATISTICS_ENTRY.SUM_Z.value,
        cle.STATISTICS_ENTRY.SUM_DISTANCE_TO_MASS_CENTER.value,
        cle.STATISTICS_ENTRY.MEAN_DISTANCE_TO_MASS_CENTER.value,
        cle.STATISTICS_ENTRY.MAX_DISTANCE_TO_MASS_CENTER.value,
        cle.STATISTICS_ENTRY.MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO.value,

    ]
    for column_index in columns_to_test:
        reference_values = clij_reference_table[:, column_index]
        values = table[:, column_index]
        print("testing STATISTICS_ENTRY" + str( cle.STATISTICS_ENTRY(column_index)))
        print(reference_values)
        print(values)
        assert np.allclose(reference_values, values, 0.001)

def test_statistics_of_background_and_labelled_pixels_gpu_compare_to_clij2():
    from skimage.io import imread

    blobs = cle.push_zyx(imread('data/mini_blobs.tif'))
    labels = cle.push_zyx(imread('data/mini_blobs_otsu_labels_excluded_edges_imagej.tif'))

    regionprops = cle.statistics_of_background_and_labelled_pixels(blobs, labels, use_gpu=True)
    table = cle.pull_zyx(cle.transpose_xy(cle.push_regionprops(regionprops)))


    print(table)

    import numpy as np
    # np.savetxt('../data/mini_blobs_measurements_pyclesperanto.csv', table,delimiter=',')
    clij_reference_table = np.loadtxt('data/mini_blobs_measurements_clij.csv', delimiter=',', skiprows=1)
    # chop off first column as ImageJ saved an additional counter column
    clij_reference_table = clij_reference_table[:, 1:]

    print(clij_reference_table)

    columns_to_test = [
        cle.STATISTICS_ENTRY.IDENTIFIER.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_X.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_Y.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_Z.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_END_X.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_END_Y.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_END_Z.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_WIDTH.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_HEIGHT.value,
        cle.STATISTICS_ENTRY.BOUNDING_BOX_DEPTH.value,
        cle.STATISTICS_ENTRY.MINIMUM_INTENSITY.value,
        cle.STATISTICS_ENTRY.MAXIMUM_INTENSITY.value,
        cle.STATISTICS_ENTRY.MEAN_INTENSITY.value,
        cle.STATISTICS_ENTRY.SUM_INTENSITY.value,
        cle.STATISTICS_ENTRY.STANDARD_DEVIATION_INTENSITY.value,
        cle.STATISTICS_ENTRY.PIXEL_COUNT.value,
        cle.STATISTICS_ENTRY.MASS_CENTER_X.value,
        cle.STATISTICS_ENTRY.MASS_CENTER_Y.value,
        cle.STATISTICS_ENTRY.MASS_CENTER_Z.value,
        cle.STATISTICS_ENTRY.CENTROID_X.value,
        cle.STATISTICS_ENTRY.CENTROID_Y.value,
        cle.STATISTICS_ENTRY.CENTROID_Z.value,
        cle.STATISTICS_ENTRY.SUM_DISTANCE_TO_CENTROID.value,
        cle.STATISTICS_ENTRY.MEAN_DISTANCE_TO_CENTROID.value,
        cle.STATISTICS_ENTRY.MAX_DISTANCE_TO_CENTROID.value,
        cle.STATISTICS_ENTRY.MAX_MEAN_DISTANCE_TO_CENTROID_RATIO.value,
        cle.STATISTICS_ENTRY.SUM_INTENSITY_TIMES_X.value,
        cle.STATISTICS_ENTRY.SUM_INTENSITY_TIMES_Y.value,
        cle.STATISTICS_ENTRY.SUM_INTENSITY_TIMES_Z.value,
        cle.STATISTICS_ENTRY.SUM_X.value,
        cle.STATISTICS_ENTRY.SUM_Y.value,
        cle.STATISTICS_ENTRY.SUM_Z.value,
        cle.STATISTICS_ENTRY.SUM_DISTANCE_TO_MASS_CENTER.value,
        cle.STATISTICS_ENTRY.MEAN_DISTANCE_TO_MASS_CENTER.value,
        cle.STATISTICS_ENTRY.MAX_DISTANCE_TO_MASS_CENTER.value,
        cle.STATISTICS_ENTRY.MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO.value,
    ]

    for column_index in columns_to_test:
        reference_values = clij_reference_table[:, column_index]
        values = table[:, column_index]
        print("testing STATISTICS_ENTRY" + str( cle.STATISTICS_ENTRY(column_index)))
        print(reference_values)
        print(values)
        assert np.allclose(reference_values, values, 0.001)
