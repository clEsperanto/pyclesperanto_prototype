def test_iterator():
    import pyclesperanto_prototype as cle
    import numpy as np

    image = np.random.random((3, 2, 5))
    cle_image = cle.asarray(image)

    for i, j in zip(image, cle_image):
        print(cle.array_equal(i,j))

        assert cle.array_equal(i,j)

def test_enumerate():
    import pyclesperanto_prototype as cle

    cle_array = cle.create((2, 10))
    cle.set_ramp_x(cle_array)

    sum_ = 0
    for i, y in enumerate(cle_array[0]):
        print(i, y)
        sum_ += y

    assert sum_ == 45

def test_zip():
    import pyclesperanto_prototype as cle

    cle_array = cle.create((2, 10))
    cle.set_ramp_x(cle_array)

    sum_ = 0
    for x, y in zip(cle_array[0], cle_array[1]):
        print(x, y)
        sum_ += y

    assert sum_ == 45
