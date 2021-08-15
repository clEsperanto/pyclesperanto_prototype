def test_np_asarray():
    import pyclesperanto_prototype as cle

    import numpy as np
    data = np.asarray([[[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]]).astype(np.float32)

    cl_data = cle.push(data)

    assert data.dtype == cl_data.dtype

    assert data.dtype == np.asarray(cl_data.dtype)

    labels = cle.voronoi_otsu_labeling(cl_data)
    print(labels.dtype)
    print(np.asarray(labels).dtype)

    assert labels.dtype == np.asarray(labels).dtype

