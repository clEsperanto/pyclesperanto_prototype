def test_skimage_imsave():
    import pyclesperanto_prototype as cle
    import numpy as np

    image = cle.push(np.asarray([
            [1, 2],
            [3, 4]
        ]))

    from skimage.io import imsave
    imsave('test.tif', image)