def test_cupy_compatibility():
    import pytest
    cupy = pytest.importorskip('cupy')

    import pyclesperanto_prototype as cle
    import numpy as np

    np_arr = np.random.random((100, 100))
    cp_arr = cupy.asarray(np_arr)
    cl_arr = cle.asarray(np_arr)

    a = cl_arr + np_arr
    b = cle.add_images(cl_arr, cp_arr)
    c = np_arr + np_arr

    assert np.allclose(c, a)
    assert np.allclose(c, b)
