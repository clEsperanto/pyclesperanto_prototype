import cupy
import numpy as np
from ._cuda_execute import execute
from ._array_operators import ArrayOperators

def cuda_backend():
    return CUDABackend()


class CUDABackend():
    def __init__(self):
        pass

    def array_type(self):
        return cupy._core.core.ndarray

    def asarray(self, image):
        return np.asarray(image.get())

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        return cupy._core.core.ndarray(shape, dtype)

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)

    def from_array(cls, arr, *args, **kwargs):
        return cupy.asarray(arr)


