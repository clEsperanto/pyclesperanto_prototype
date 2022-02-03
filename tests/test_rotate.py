import pyclesperanto_prototype as cle
import numpy as np

def test_rotate():
    source = cle.push(np.asarray([[
          [0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]]))

    result = cle.rotate(source, angle_around_z_in_degrees=45.0, rotate_around_center=False)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_rotate_around_center():
    source = cle.push(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]]))

    result = cle.rotate(source, angle_around_z_in_degrees=90.0, rotate_around_center=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_rotation_auto_size():
    source = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]]))

    result = cle.rotate(source, angle_around_z_in_degrees=45, auto_size=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_rotate_around_z_center():
    source = np.zeros((5,5,5))
    source[2, 2, 4] = 1

    reference = np.zeros((5,5,5))
    reference[2,4,2] = 1

    transform = cle.AffineTransform3D()
    transform.center(source.shape)
    transform.rotate_around_z_axis(90)
    transform.center(source.shape, undo=True)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_rotate_around_y_center():
    source = np.zeros((5,5,5))
    source[2, 2, 0] = 1

    reference = np.zeros((5,5,5))
    reference[4,2,2] = 1

    transform = cle.AffineTransform3D()
    transform.center(source.shape)
    transform.rotate_around_y_axis(90)
    transform.center(source.shape, undo=True)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_rotate_around_x_center():
    source = np.zeros((5,5,5))
    source[2, 0, 2] = 1

    reference = np.zeros((5,5,5))
    reference[0,2,2] = 1

    transform = cle.AffineTransform3D()
    transform.center(source.shape)
    transform.rotate_around_x_axis(90)
    transform.center(source.shape, undo=True)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

