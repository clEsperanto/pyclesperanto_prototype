def test_dask_compatibility():
    import pytest
    array = pytest.importorskip('dask.array')
    import pyclesperanto_prototype as cle
    import numpy as np


    np_arr = np.random.random((100, 100))
    da_arr = array.from_array(np_arr)
    cl_arr = cle.asarray(np_arr)

    a = cl_arr + np_arr
    b = cle.add_images(cl_arr, da_arr)
    c = np_arr + np_arr

    assert np.allclose(c, a)
    assert np.allclose(c, b)
