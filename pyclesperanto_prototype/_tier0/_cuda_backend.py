import cupy
import numpy as np
from ._cuda_execute import execute

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
        return cupy.empty(shape, dtype)

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)

class CUDAArray():

    @classmethod
    def from_array(cls, arr, *args, **kwargs):
        return cupy.asarray(arr)


