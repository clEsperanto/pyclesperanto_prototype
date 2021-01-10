import pyclesperanto_prototype as cle
import numpy as np

def test_histogram():
    test = cle.push_zyx(np.asarray([
        [1, 2, 4, 4, 2, 3],
        [3, 3, 4, 4, 5, 5]
    ]))

    ref_histogram = [[1, 2, 3, 4, 2]]

    my_histogram = cle.histogram(test, num_bins = 5)

    print(my_histogram)

    a = cle.pull_zyx(my_histogram)
    assert (np.allclose(a, ref_histogram))

def test_histogram_3d():
    test = cle.push_zyx(np.asarray([
        [
            [1, 2, 4, 4, 2, 3]
        ], [
            [3, 3, 4, 4, 5, 5]
        ]
    ]))

    ref_histogram = [1, 2, 3, 4, 2]

    my_histogram = cle.histogram(test, num_bins = 5)

    print(my_histogram)

    a = cle.pull_zyx(my_histogram)
    assert (np.allclose(a, ref_histogram))


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

    my_histogram = cle.histogram(test, num_bins = 5)

    print(my_histogram)

    a = cle.pull_zyx(my_histogram)
    assert (np.allclose(a, ref_histogram))

def test_histogram_against_scikit_image():
    from skimage.data import camera
    image = camera()

    from skimage import exposure
    hist, bc = exposure.histogram(image.ravel(), 256, source_range='image')

    print(str(hist))

    gpu_image = cle.push_zyx(image)

    gpu_hist = cle.histogram(gpu_image, num_bins=256)

    print(str(cle.pull_zyx(gpu_hist)))

    assert (np.allclose(hist, cle.pull_zyx(gpu_hist)))

