import pyclesperanto_prototype as cle
import numpy as np

def test_affine_transform_translate():
    source = cle.push(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    transform = cle.AffineTransform3D()
    transform.translate(-1, -1, 0)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_transform_scale():
    source = cle.push(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]]))

    transform = cle.AffineTransform3D()
    transform.scale(1, 2, 1)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_affine_transform_scale_with_transform_matrix():
    source = cle.push(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]]))

    transform = np.asarray([
        [1, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_transform_rotate():
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

    transform = cle.AffineTransform3D()
    transform.rotate(2, 45.0)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_affine_transform_rotate_around_center():
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

    transform = cle.AffineTransform3D()
    transform.translate(-2.5, -2.5)
    transform.rotate(2, 90.0)
    transform.translate(2.5, 2.5)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_affine_transform_rotation_auto_size():
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

    transform = cle.AffineTransform3D()
    transform.rotate(angle_in_degrees=45)

    result = cle.affine_transform(source, transform=transform, auto_size=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


    
def test_affine_transform_make_sure_2d_images_become_2d_results():
    source = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]))

    transform = cle.AffineTransform3D()
    transform.translate(-1, -1, 0)

    result = cle.affine_transform(source, transform=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

    

    
def test_affine_transform_make_sure_2d_images_become_2d_results_autosize():
    source = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]))

    transform = cle.AffineTransform3D()

    result = cle.affine_transform(source, transform=transform, auto_size=True)

    a = cle.pull(result)
    b = cle.pull(source)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
