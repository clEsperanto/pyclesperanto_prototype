def test_dask_compatibility():
    try:
        from dask import array
    except ImportError:
        # dask may not be installed in the CI
        return
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
