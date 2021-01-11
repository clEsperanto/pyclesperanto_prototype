import pyclesperanto_prototype as cle
import numpy as np

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

    result = cle.rotate(source, angle_around_z_in_degrees=45.0, rotate_around_center=False)

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

    result = cle.rotate(source, angle_around_z_in_degrees=90.0, rotate_around_center=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_rotate_compare_with_scipy():
    import numpy as np
    source = np.asarray([
        [
          [0, 0, 0],
          [0, 0, 0],
          [0, 1, 1],
        ], [
          [0, 0, 0],
          [0, 0, 0],
          [0, 1, 1],
        ], [
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
        ]
    ])

    import scipy

    angle = 90
    axes = [0, 1]
    reference = scipy.ndimage.rotate(source, angle=angle, axes=axes)
    result = cle.rotate(source, angle=angle, axes=axes)
    np.allclose(result, reference, 0.001)

    angle = 90
    axes = [1, 0]
    reference = scipy.ndimage.rotate(source, angle=angle, axes=axes)
    result = cle.rotate(source, angle=angle, axes=axes)
    np.allclose(result, reference, 0.001)

    angle = 90
    axes = [0, 2]
    reference = scipy.ndimage.rotate(source, angle=angle, axes=axes)
    result = cle.rotate(source, angle=angle, axes=axes)
    np.allclose(result, reference, 0.001)

    angle = 90
    axes = [2, 0]
    reference = scipy.ndimage.rotate(source, angle=angle, axes=axes)
    result = cle.rotate(source, angle=angle, axes=axes)
    np.allclose(result, reference, 0.001)

    angle = 90
    axes = [1, 2]
    reference = scipy.ndimage.rotate(source, angle=angle, axes=axes)
    result = cle.rotate(source, angle=angle, axes=axes)
    np.allclose(result, reference, 0.001)

    angle = 90
    axes = [2, 1]
    reference = scipy.ndimage.rotate(source, angle=angle, axes=axes)
    result = cle.rotate(source, angle=angle, axes=axes)
    np.allclose(result, reference, 0.001)
