import warnings

import cupy
import numpy as np
from ._cuda_execute import execute

def cuda_backend():
    return CUDABackend()


class CUDABackend():
    def __init__(self):
        self.first_run = True
        pass

    def array_type(self):
        return (CUDAArray, cupy._core.core.ndarray)

    def asarray(self, image):
        if isinstance(image, np.ndarray):
            return image
        return np.asarray(image.get())

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        return CUDAArray(cupy._core.core.ndarray(shape, dtype))

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog = None, constants = None, image_size_independent_kernel_compilation : bool = None, device = None):
        if self.first_run:
            self.first_run = False
            warnings.warn("clesperanto's cupy / CUDA backend is experimental. Please use it with care. The following functions are known to cause issues in the CUDA backend:\n" +
                          "affine_transform, apply_vector_field, create(uint64), create(int32), create(int64), label_spots, labelled_spots_to_pointlist, resample, scale, spots_to_pointlist"
                          )
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)

    def from_array(cls, arr, *args, **kwargs):
        return CUDAArray(cupy.asarray(arr))

    def __str__(self):
        return "cupy backend (experimental)"

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
    def ndim(self):
        return self.array.ndim

    def get(self, *args, **kwargs):
        return self.array.get(*args, **kwargs)

    def __array__(self, dtype=None):
        if dtype is None:
            return self.array.get()
        else:
            return self.array.get().astype(dtype)

    def __repr__(self):
        return "experimental clesperanto CUDAArray(" + str(self.array.get()) + ", dtype=" + str(self.array.dtype) + ")"

