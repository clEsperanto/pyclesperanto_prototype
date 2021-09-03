def test_skimage_imsave():
    import pyclesperanto_prototype as cle
    image = cle.push([1, 2, 3])

    from skimage.io import imsave
    imsave('test.tif', image)