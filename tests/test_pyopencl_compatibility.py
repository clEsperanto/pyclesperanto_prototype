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