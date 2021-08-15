def test_ocl_array_getitem_3d():
    import pyclesperanto_prototype as cle

    import numpy as np
    data = np.asarray([[[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]]).astype(np.float32)
    ref = np.asarray([[1.0, 2.0, 1.0]]).astype(np.float32)

    cl_data = cle.push(data)

    positions = (
        np.asarray([0, 0, 0]),
        np.asarray([0, 1, 1]),
        np.asarray([0, 1, 0])
    )

    values = cl_data[positions]

    assert(np.allclose(values, ref))

def test_ocl_array_getitem_2d():
    import pyclesperanto_prototype as cle

    import numpy as np
    data = np.asarray([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]).astype(np.float32)
    ref = np.asarray([[[1.0, 2.0, 2.0]]]).astype(np.float32)

    cl_data = cle.push(data)

    positions = (
        np.asarray([0, 1, 0]),
        np.asarray([0, 1, 1])
    )

    values = cl_data[positions]

    assert(np.allclose(values, ref))
