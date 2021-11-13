import numpy as np

from ._device import get_device
from ._pycl import OCLArray, assert_supported_ndarray_type


def opencl_backend():
    return OpenCLBackend()

class OpenCLBackend():
    def __init__(self):
        pass

    def array_type(self):
        return OCLArray

    def asarray(self, image):
        return np.asarray(image)

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        assert_supported_ndarray_type(dtype)
        queue = get_device().queue
        return OCLArray(queue, shape, dtype)
