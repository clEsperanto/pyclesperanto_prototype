def test_pyopencl_compatibility():
    import numpy as np
    import pyopencl as cl
    import pyopencl.array as cla

    # initialize GPU driver and create a queue for running operations.
    context = cl.create_some_context()
    queue = cl.CommandQueue(context)

    # copy data to GPU memory
    cl_a = cla.to_device(queue, np.asarray([[[[1, 2, 3]]]]))
    cl_b = cla.to_device(queue, np.asarray([[[[4, 4, 5]]]]))

    # execute operations on the data
    cl_c = cl_a + cl_b

    import pyclesperanto_prototype as cle
    cl_c = cl_a + cl_b

def test_semi_push():
    import numpy as np
    img = np.asarray([[1,2],[3,4], [5,6]])

    import pyclesperanto_prototype as cle
    device = cle.get_device()

    import pyopencl.array as cla
    pushed = cla.to_device(device.queue, img)

    print(type(pushed))
    print(pushed.shape)
    blurred = cle.gaussian_blur(pushed, sigma_x=10, sigma_y=10, sigma_z=10)

    assert np.array_equal(blurred.shape, pushed.shape)

