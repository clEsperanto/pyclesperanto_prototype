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

    def empty_image_like(self, arr, ctx=None, *args, **kwargs):
        if ctx is None:
            ctx = get_device().context
        from ._cl_image import empty_image
        return empty_image(ctx, arr.shape, arr.dtype)

    def empty(self, shape, dtype=np.float32):
        assert_supported_ndarray_type(dtype)
        queue = get_device().queue
        return OCLArray(queue, shape, dtype)

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog = None, constants = None, image_size_independent_kernel_compilation : bool = None, device = None):
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog, constants, image_size_independent_kernel_compilation, device)

    def from_array(self, *args, **kwargs):
        return OCLArray.from_array(*args, **kwargs)