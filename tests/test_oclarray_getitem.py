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

def test_clamp_to_edge():
    import pyclesperanto_prototype as cle

    import numpy as np

    x = cle.push([[np.arange(10)]])
    print(x.shape)

    positions = (
        np.asarray([0]),
        np.asarray([0]),
        np.asarray([20])
    )

    assert x[positions] == 9

def test_tuple():
    import pyclesperanto_prototype as cle

    import numpy as np

    x = cle.push([[np.arange(10)]])
    print(x.shape)

    positions = (
        np.asarray([0]),
        np.asarray([0]),
        np.asarray([4])
    )

    assert x[positions] == 4

def test_tuple2():
    import pyclesperanto_prototype as cle

    import numpy as np

    x = cle.push([[np.arange(10)]])
    print(x.shape)

    positions = (0, 0, 4)

    assert x[positions] == 4

def test_list():
    import pyclesperanto_prototype as cle

    import numpy as np

    x = cle.push([[np.arange(10)]])
    print(x.shape)

    positions = [0, 0, 4]

    assert x[positions] == 4

def test_list2():
    import pyclesperanto_prototype as cle

    import numpy as np

    x = cle.push([[np.arange(10)]])
    print(x.shape)

    positions = [[0, 0], [0, 0], [4, 5]]

    assert np.allclose(x[positions], [4, 5])


def test_list_tuple_mix():
    import pyclesperanto_prototype as cle

    import numpy as np

    x = cle.push([[np.arange(10)]])
    print(x.shape)

    positions = [(0, 0), (0, 0), (4, 5)]

    assert np.allclose(x[positions], [4, 5])

def test_list_tuple_mix2():
    import pyclesperanto_prototype as cle

    import numpy as np

    x = cle.push([[np.arange(10)]])
    print(x.shape)

    positions = ([0, 0], [0, 0], [4, 5])

    assert np.allclose(x[positions], [4, 5])