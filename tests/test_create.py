import numpy as np
import pyclesperanto_prototype as cle

def test_create_3d():
    size = [2, 3, 4]

    image = cle.create(size)

    assert (image.shape[0] == 2)
    assert (image.shape[1] == 3)
    assert (image.shape[2] == 4)

    image2 = cle.create_like(image)
    assert (image2.shape[0] == 2)
    assert (image2.shape[1] == 3)
    assert (image2.shape[2] == 4)

def test_create_2d():
    size = [2, 3]

    image = cle.create(size)

    assert (image.shape[0] == 2)
    assert (image.shape[1] == 3)

    image2 = cle.create_like(image)
    assert (image2.shape[0] == 2)
    assert (image2.shape[1] == 3)

def test_create_uint8():
    image = cle.push([
        [-1, 1.5],
        [ 2000, -7.8]
    ])
    reference = np.asarray([
        [0, 1],
        [255, 0]
    ])

    target = cle.create(image.shape, dtype=np.uint8)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)

def test_create_uint16():
    image = cle.push([
        [-1, 1.5],
        [ 2000, -7.8]
    ])
    reference = np.asarray([
        [0, 1],
        [2000, 0]
    ])

    target = cle.create(image.shape, dtype=np.uint16)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)


def test_create_uint32():
    image = cle.push([
        [-1, 1.5],
        [ 2000, -7.8]
    ])
    reference = np.asarray([
        [0, 1],
        [2000, 0]
    ])

    target = cle.create(image.shape, dtype=np.uint32)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)




def test_create_uint64():
    image = cle.push([
        [-1, 1.5],
        [ 2000, -7.8]
    ])
    reference = np.asarray([
        [0, 1],
        [2000, 0]
    ])

    target = cle.create(image.shape, dtype=np.uint64)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)




def test_create_int8():
    image = cle.push([
        [-1, 1.5],
        [ 2000, -7.8]
    ])
    reference = np.asarray([
        [-1, 1],
        [127, -7]
    ])

    target = cle.create(image.shape, dtype=np.int8)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)

def test_create_int16():
    image = cle.push([
        [-1, 1.5],
        [ 2000, -7.8]
    ])
    reference = np.asarray([
        [-1, 1],
        [2000, -7]
    ])

    target = cle.create(image.shape, dtype=np.int16)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)

def test_create_int32():
    image = cle.push([
        [-1, 1.5],
        [ 200000, -7.8]
    ])
    reference = np.asarray([
        [-1, 1],
        [200000, -7]
    ])

    target = cle.create(image.shape, dtype=np.int32)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)

def test_create_int64():
    image = cle.push([
        [-1, 1.5],
        [ 2000, -7.8]
    ])
    reference = np.asarray([
        [-1, 1],
        [2000, -7]
    ])

    target = cle.create(image.shape, dtype=np.int64)

    cle.copy(image, target)

    print(target)

    assert np.allclose(target, reference)

def test_create_like_numpy():
    import pyclesperanto_prototype as cle
    import numpy

    image = numpy.random.random((10,20))

    cle_image = cle.create_like(image)
    cle.copy(image, cle_image)

    assert cle.array_equal(image, cle_image)
