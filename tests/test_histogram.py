import pyclesperanto_prototype as cle
import numpy as np

def test_histogram():
    test = cle.push_zyx(np.asarray([
        [1, 2, 4, 4, 2, 3],
        [3, 3, 4, 4, 5, 5]
    ]))

    ref_histogram = [1, 2, 3, 4, 2]

    # todo: this line should not be necessary. cle.histogram should be able to create this with correct size itself
    my_histogram = cle.push_zyx(np.asarray([0, 0, 0, 0, 0]))

    my_histogram = cle.histogram(test, hist=my_histogram, num_bins = 5)

    print(my_histogram)

    a = cle.pull(my_histogram)
    assert (np.allclose(a, ref_histogram))
    print ("ok histogram")

def test_histogram_3d():
    test = cle.push_zyx(np.asarray([
        [
            [1, 2, 4, 4, 2, 3]
        ], [
            [3, 3, 4, 4, 5, 5]
        ]
    ]))

    ref_histogram = [1, 2, 3, 4, 2]

    # todo: this line should not be necessary. cle.histogram should be able to create this with correct size itself
    my_histogram = cle.push_zyx(np.asarray([0, 0, 0, 0, 0]))

    my_histogram = cle.histogram(test, hist=my_histogram, num_bins = 5)

    print(my_histogram)

    a = cle.pull(my_histogram)
    assert (np.allclose(a, ref_histogram))
    print ("ok histogram")


def test_histogram_3d_2():
    test = cle.push_zyx(np.asarray([
        [
            [1, 2, 4],
            [4, 2, 3]
        ], [
            [3, 3, 4],
            [4, 5, 5]
        ]
    ]))

    ref_histogram = [1, 2, 3, 4, 2]

    # todo: this line should not be necessary. cle.histogram should be able to create this with correct size itself
    my_histogram = cle.push_zyx(np.asarray([0, 0, 0, 0, 0]))

    my_histogram = cle.histogram(test, hist=my_histogram, num_bins = 5)

    print(my_histogram)

    a = cle.pull(my_histogram)
    assert (np.allclose(a, ref_histogram))
    print ("ok histogram")

