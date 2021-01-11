import pyclesperanto_prototype as cle
import numpy as np


def test_scale_centered():
    source = cle.push(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    result = cle.scale(source, factor_y=2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_scale_not_centered():
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
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    result = cle.scale(source, factor_y=2, centered=False)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_scale_compare_with_scipy():
    import numpy as np
    source = np.asarray([
        [
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
        ], [
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
        ], [
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
        ], [
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
        ]
    ])

    import scipy
    import numpy as np

    zoom = [1, 2, 1]
    reference = scipy.ndimage.zoom(source, zoom=zoom)
    result = cle.zoom(source, zoom=zoom)
    assert np.allclose(result, reference, 0.001)

    zoom = [1, 0.5, 1]
    reference = scipy.ndimage.zoom(source, zoom=zoom)
    result = cle.zoom(source, zoom=zoom)
    assert np.allclose(result, reference, 0.001)

    zoom = [2, 1, 1]
    reference = scipy.ndimage.zoom(source, zoom=zoom)
    result = cle.zoom(source, zoom=zoom)
    assert np.allclose(result, reference, 0.001)

    zoom = [0.5, 1, 1]
    reference = scipy.ndimage.zoom(source, zoom=zoom)
    result = cle.zoom(source, zoom=zoom)
    assert np.allclose(result, reference, 0.001)

    zoom = [1, 1, 2]
    reference = scipy.ndimage.zoom(source, zoom=zoom)
    result = cle.zoom(source, zoom=zoom)
    assert np.allclose(result, reference, 0.001)

# for this one, we need a different image to make scipy output something reasonable.
# in practice, this should not matter
def test_scale_compare_with_scipy_failing():
    import numpy as np
    source = np.asarray([
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ], [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ], [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ], [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    ])

    import scipy
    import numpy as np

    zoom = [1, 1, 0.5]
    reference = scipy.ndimage.zoom(source, zoom=zoom)
    result = cle.zoom(source, zoom=zoom)
    assert np.allclose(result, reference, 0.001)