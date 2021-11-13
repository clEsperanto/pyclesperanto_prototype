import cupy
import numpy as np
from ._cuda_execute import execute

def cuda_backend():
    return CUDABackend()


class CUDABackend():
    def __init__(self):
        pass

    def array_type(self):
        return (CUDAArray, cupy._core.core.ndarray)

    def asarray(self, image):
        return np.asarray(image.get())

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        return CUDAArray(cupy._core.core.ndarray(shape, dtype))

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)

    def from_array(cls, arr, *args, **kwargs):
        return CUDAArray(cupy.asarray(arr))

from ._array_operators import ArrayOperators
class CUDAArray(ArrayOperators, np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, array):
        self.array = array

    def get_array(self):
        return self.array

    @property
    def shape(self):
        return self.array.shape

    @property
    def size(self):
        return self.array.size

    @property
    def dtype(self):
        return self.array.dtype

    @property
    def ndims(self):
        return self.array.ndims

    def get(self, *args, **kwargs):
        return self.array.get(*args, **kwargs)

    def __array__(self, dtype=None):
        if dtype is None:
            return self.array.get()
        else:
            return self.array.get().astype(dtype)

