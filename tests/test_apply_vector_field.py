import pyclesperanto_prototype as cle
import numpy as np

def test_apply_vector_field_3d():
    source = cle.push(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, 2, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0],
    ]]))

    vector_x = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0.5, 1.0, 0.5, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0, 0, 0, 0],
    ]]))

    vector_y = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    vector_z = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 2, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    result = cle.apply_vector_field(source, vector_x,vector_y,vector_z)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_apply_vector_field_3d_linear_interpolation():
    source = cle.push(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, 2, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0],
    ]]))

    vector_x = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0.5, 1.0, 0.5, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0, 0, 0, 0],
    ]]))

    vector_y = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    vector_z = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0.5, 0],
        [0, 1.5, 1, 0.5, 0],
        [0, 1, 1, 0.5, 0],
        [0, 0, 0, 0, 0],
    ]]))

    result = cle.apply_vector_field(source, vector_x,vector_y,vector_z, linear_interpolation=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_apply_vector_field_2d():
    source = cle.push(np.asarray([
          [0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, 2, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0],
    ]))

    vector_x = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0.5, 1.0, 0.5, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0, 0, 0, 0],
    ]))

    vector_y = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 2, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]))

    result = cle.apply_vector_field(source, vector_x,vector_y)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_apply_vector_field_2d_linear_interpolation():
    source = cle.push(np.asarray([
          [0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, 2, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0],
    ]))

    vector_x = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0.5, 1.0, 0.5, 0],
        [0, 0.5, 0.5, 0.5, 0],
        [0, 0, 0, 0, 0],
    ]))

    vector_y = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0.5, 0],
        [0, 1.5, 1, 0.5, 0],
        [0, 1, 1, 0.5, 0],
        [0, 0, 0, 0, 0],
    ]))

    result = cle.apply_vector_field(source, vector_x,vector_y, linear_interpolation=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))




