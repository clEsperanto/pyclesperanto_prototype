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
        return CUDAArray

    def asarray(self, image):
        return np.asarray(image.get())

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        return CUDAArray(shape, dtype)

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)

class CUDAArray(ArrayOperators, cupy._core.core.ndarray, np.lib.mixins.NDArrayOperatorsMixin):

    @classmethod
    def from_array(cls, arr, *args, **kwargs):
        source = cupy.asarray(arr)
        destination = CUDAArray(source.shape, source.dtype)
        from .._tier0 import execute
        parameters = {
            "dst": destination,
            "src": source
        }
        execute(__file__, '../clij-opencl-kernels/kernels/copy_' + str(len(destination.shape)) + 'd_x.cl',
                'copy_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
        return destination



