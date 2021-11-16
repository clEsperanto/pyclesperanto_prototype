import warnings

import cupy
import numpy as np
from ._cuda_execute import execute

def cuda_backend():
    return CUDABackend()


class CUDABackend():
    def __init__(self):
        self.first_run = True
        self.first_image_access = True
        pass

    def array_type(self):
        return (CUDAArray, cupy._core.core.ndarray)

    def asarray(self, image):
        if isinstance(image, np.ndarray):
            return image
        return np.asarray(image.get())

    def empty_image_like(self, image, *args, **kwargs):
        from .._tier1 import copy
        if self.first_image_access:
            warnings.warn("CUDA image types and linear interpolation are not supported yet.")
            self.first_image_access = False
        return copy(image)

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        return CUDAArray(cupy._core.core.ndarray(shape, dtype))

    def execute(self, anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog = None, constants = None, image_size_independent_kernel_compilation : bool = None, device = None):
        if self.first_run:
            self.first_run = False
            warnings.warn("clesperanto's cupy / CUDA backend is experimental. Please use it with care. The following functions are known to cause issues in the CUDA backend:\n" +
                          "affine_transform, apply_vector_field, create(uint64), create(int32), create(int64), resample, scale, spots_to_pointlist"
                          )
        return execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)

    def from_array(cls, arr, *args, **kwargs):
        return CUDAArray(cupy.asarray(arr))

    def __str__(self):
        return "cupy backend (experimental)"

from ._array_operators import ArrayOperators, _supported_numeric_types
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

    def min(self, axis=None, out=None):
        from .._tier2 import minimum_of_all_pixels
        from .._tier1 import minimum_x_projection
        from .._tier1 import minimum_y_projection
        from .._tier1 import minimum_z_projection

        if axis==0:
            result = minimum_z_projection(self)
        elif axis==1:
            result = minimum_y_projection(self)
        elif axis==2:
            result = minimum_x_projection(self)
        elif axis is None:
            result = minimum_of_all_pixels(self)
        else:
            raise ValueError("Axis " + axis + " not supported")
        if out is not None:
            np.copyto(out, result.get().astype(out.dtype))
        return result

    def max(self, axis=None, out=None):
        from .._tier2 import maximum_of_all_pixels
        from .._tier1 import maximum_x_projection
        from .._tier1 import maximum_y_projection
        from .._tier1 import maximum_z_projection

        if axis==0:
            result = maximum_z_projection(self)
        elif axis==1:
            result = maximum_y_projection(self)
        elif axis==2:
            result = maximum_x_projection(self)
        elif axis is None:
            result = maximum_of_all_pixels(self)
        else:
            raise ValueError("Axis " + axis + " not supported")
        if out is not None:
            np.copyto(out, result.get().astype(out.dtype))
        return result

    def sum(self, axis=None, out=None):
        from .._tier2 import sum_of_all_pixels
        from .._tier1 import sum_x_projection
        from .._tier1 import sum_y_projection
        from .._tier1 import sum_z_projection

        if axis==0:
            result = sum_z_projection(self)
        elif axis==1:
            result = sum_y_projection(self)
        elif axis==2:
            result = sum_x_projection(self)
        elif axis is None:
            result = sum_of_all_pixels(self)
        else:
            raise ValueError("Axis " + axis + " not supported")
        if out is not None:
            np.copyto(out, result.get().astype(out.dtype))
        return result

    def __iadd__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(temp, x2, x1)

    def __isub__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(x1, scalar=-x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(x1, x2, factor2=-1)

    def __div__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(x1, scalar=1.0 / x2)
        else:
            from .._tier1 import divide_images
            return divide_images(x1, x2)

    def __truediv__(x1, x2):
        return x1.__div__(x2)

    def __idiv__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
        else:
            from .._tier1 import divide_images
            return divide_images(temp, x2, x1)

    def __itruediv__(x1, x2):
        return x1.__idiv__(x2)

    def __mul__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(x1, x2)

    def __imul__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(temp, x2, x1)

    def __gt__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import greater_constant
            return greater_constant(x1, constant=x2)
        else:
            from .._tier1 import greater
            return greater(x1, x2)

    def __ge__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import greater_or_equal_constant
            return greater_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import greater_or_equal
            return greater_or_equal(x1, x2)

    def __lt__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import smaller_constant
            return smaller_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller
            return smaller(x1, x2)

    def __le__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import smaller_or_equal_constant
            return smaller_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller_or_equal
            return smaller_or_equal(x1, x2)

    def __eq__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import equal_constant
            return equal_constant(x1, constant=x2)
        else:
            from .._tier1 import equal
            return equal(x1, x2)

    def __ne__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import not_equal_constant
            return not_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import not_equal
            return not_equal(x1, x2)

    def __pow__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import power
            return power(x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(x1, x2)

    def __ipow__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import power
            return power(temp, x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(temp, x2, x1)



