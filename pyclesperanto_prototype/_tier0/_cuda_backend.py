import cupy
import numpy as np

def cuda_backend():
    return CUDABackend()


class CUDABackend():
    def __init__(self):
        pass

    def array_type(self):
        return CUDAArray

    def asarray(self, image):
        return np.asarray(image.get())


class CUDAArray():

    @classmethod
    def from_array(cls, arr, *args, **kwargs):
        return cupy.asarray(arr)
