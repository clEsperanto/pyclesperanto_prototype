import pyclesperanto_prototype as cle
import numpy as np

def test_translate():
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

    result = cle.translate(source, translate_x=-1, translate_y=-1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_translate_compare_with_scipy():
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

    vector = [-1, 0, 0]
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = [1, 0, 0]
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = [0, 1, 0]
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = [0, -1, 0]
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = [0, 0, 1]
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = [0, 0, -1]
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = 1.
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = -1.
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = 1
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)

    vector = -1
    reference = scipy.ndimage.shift(source, shift=vector)
    result = cle.shift(source, shift=vector)
    np.allclose(result, reference, 0.001)
