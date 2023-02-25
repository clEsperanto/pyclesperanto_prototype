def test_iterator():
    import pyclesperanto_prototype as cle
    import numpy as np

    image = np.random.random((3, 2, 5))
    cle_image = cle.asarray(image)

    for i, j in zip(image, cle_image):
        print(cle.array_equal(i,j))

        assert cle.array_equal(i,j)
