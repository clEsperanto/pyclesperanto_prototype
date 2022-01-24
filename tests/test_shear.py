import pyclesperanto_prototype as cle
import numpy as np


def test_affine_shear_y_in_x_plane():
    source = np.zeros((5, 5, 5))
    source[1, 1, 1] = 1

    reference = np.zeros((5, 5, 5))
    reference[1, 2, 1] = 1

    transform = cle.AffineTransform3D()
    transform.shear_in_x_plane(angle_y_in_degrees=45)
    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_shear_z_in_x_plane():
    source = np.zeros((5, 5, 5))
    source[1, 1, 1] = 1

    reference = np.zeros((5, 5, 5))
    reference[2, 1, 1] = 1

    transform = cle.AffineTransform3D()
    transform.shear_in_x_plane(angle_z_in_degrees=45)
    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_shear_x_in_y_plane():
    source = np.zeros((5, 5, 5))
    source[1, 1, 1] = 1

    reference = np.zeros((5, 5, 5))
    reference[1, 1, 2] = 1

    transform = cle.AffineTransform3D()
    transform.shear_in_y_plane(angle_x_in_degrees=45)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_shear_z_in_y_plane():
    source = np.zeros((5, 5, 5))
    source[1, 1, 1] = 1

    reference = np.zeros((5, 5, 5))
    reference[2, 1, 1] = 1

    transform = cle.AffineTransform3D()
    transform.shear_in_y_plane(angle_z_in_degrees=45)
    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_shear_x_in_z_plane():
    source = np.zeros((5, 5, 5))
    source[1, 1, 1] = 1

    reference = np.zeros((5, 5, 5))
    reference[1, 1, 2] = 1

    transform = cle.AffineTransform3D()
    transform.shear_in_z_plane(angle_x_in_degrees=45)
    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_shear_y_in_z_plane():
    source = np.zeros((5, 5, 5))
    source[1, 1, 1] = 1

    reference = np.zeros((5, 5, 5))
    reference[1, 2, 1] = 1

    transform = cle.AffineTransform3D()
    transform.shear_in_z_plane(angle_y_in_degrees=45)
    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
