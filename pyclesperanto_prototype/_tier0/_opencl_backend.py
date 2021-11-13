import numpy as np

from ._device import get_device
from ._pycl import OCLArray, assert_supported_ndarray_type
from ._opencl_execute import execute

def opencl_backend():
    return OpenCLBackend()

class OpenCLBackend():
    def __init__(self):
        pass

    def array_type(self):
        return OCLArray

    def asarray(self, image):
        return np.asarray(image)

    def empty(self, shape, dtype=np.float32):
        assert_supported_ndarray_type(dtype)
        queue = get_device().queue
        return OCLArray(queue, shape, dtype)

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)