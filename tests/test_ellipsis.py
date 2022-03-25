def test_ellipsis():
    import pyclesperanto_prototype as cle
    import numpy as np

    image = cle.asarray([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ])
    print(image.shape, type(image))
    np_image = np.asarray([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ])
    print(image.shape, type(image))

    assert np.array_equal(   image[1, ...],
                          np_image[1, ...])

    assert np.array_equal(   image[:, 1, ...],
                          np_image[:, 1, ...])

    assert np.array_equal(   image[..., 0],
                          np_image[..., 0])



