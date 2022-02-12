def test_range1():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.asarray([
        [0, 1, 2],
        [2, 3, 4],
        [5, 6, 7]
    ]))

    reference = cle.push(np.asarray([
        [3, 4],
        [6, 7]
    ]))

    crop = image[1:, 1:]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)

def test_range2():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.asarray([
        [0, 1, 2],
        [2, 3, 4],
        [5, 6, 7]
    ]))

    reference = cle.push(np.asarray([
        [0, 1],
        [2, 3]
    ]))

    crop = image[:2, :2]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)

def test_range3():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.asarray([[
        [0, 1, 2],
        [2, 3, 4],
        [5, 6, 7]
    ]]))

    reference = cle.push(np.asarray([[
        [3, 4],
        [6, 7]
    ]]))

    crop = image[:,1:, 1:]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)

def test_range4():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.asarray([[
        [0, 1, 2],
        [2, 3, 4],
        [5, 6, 7]
    ]]))

    reference = cle.push(np.asarray([[
        [0, 1],
        [2, 3]
    ]]))

    crop = image[:,:2, :2]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)

def test_range5():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.random.random((10,20,30)))

    crop = image[:5]

    assert crop.shape[0] == 5
    assert crop.shape[1] == 20
    assert crop.shape[2] == 30

def test_range6():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.random.random((10,20,30)))

    crop = image[5]

    assert crop.shape[0] == 20
    assert crop.shape[1] == 30
    assert len(crop.shape) == 2

def test_range7():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.random.random((10,20,30)))

    crop = image[5, :]

    assert crop.shape[0] == 20
    assert crop.shape[1] == 30
    assert len(crop.shape) == 2

def test_range8():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.random.random((10,20,30)))

    crop = image[:,:, 5]

    assert crop.shape[0] == 10
    assert crop.shape[1] == 20
    assert len(crop.shape) == 2

def test_range9():
    import numpy as np
    import pyclesperanto_prototype as cle

    image = cle.push(np.random.random((10,20,30)))

    crop = image[:, 5]

    assert crop.shape[0] == 10
    assert crop.shape[1] == 30
    assert len(crop.shape) == 2

def test_range_against_numpy_1():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((2,3,4))
    input_gpu = cle.push(input)

    reference = input[1,:,:]
    result = input_gpu[1,:,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_2():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((2,3,4))
    input_gpu = cle.push(input)

    reference = input[:,1,:]
    result = input_gpu[:,1,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_3():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((2,3,4))
    input_gpu = cle.push(input)

    reference = input[:,:,1]
    result = input_gpu[:,:,1]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_4():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((2,3,4))
    input_gpu = cle.push(input)

    reference = input[1,:]
    result = input_gpu[1,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_5():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((2,3,4))
    input_gpu = cle.push(input)

    reference = input[1]
    result = input_gpu[1]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_6():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[2:5,:,:]
    result = input_gpu[2:5,:,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_7():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:,10:15,:]
    result = input_gpu[:,10:15,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_8():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:,:,10:15]
    result = input_gpu[:,:,10:15]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_9():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:5,:,:]
    result = input_gpu[:5,:,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_10():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:,:5,:]
    result = input_gpu[:,:5,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_11():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:,:,:5]
    result = input_gpu[:,:,:5]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_12():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[5:,:,:]
    result = input_gpu[5:,:,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_14():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:,5:,:]
    result = input_gpu[:,5:,:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_15():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:,:,5:]
    result = input_gpu[:,:,5:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_range_against_numpy_16():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30))
    input_gpu = cle.push(input)

    reference = input[:,:,np.int32(5)]
    result = input_gpu[:,:,np.int32(5)]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)

def test_type_1():
    import numpy as np
    import pyclesperanto_prototype as cle

    input = np.random.random((10,20,30)).astype(np.uint16)
    input_gpu = cle.push(input).astype(np.uint16)

    reference = input[:,:,np.int32(5)]
    result = input_gpu[:,:,np.int32(5)]

    print(reference)
    print(result)

    assert reference.dtype == result.dtype
