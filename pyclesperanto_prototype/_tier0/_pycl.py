import os
import sys

import numpy as np
import pyopencl as cl
from pyopencl import characterize
from pyopencl import array
from ._device import get_device

""" Below here, vendored from GPUtools
Copyright (c) 2016, Martin Weigert
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of gputools nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""





cl_image_datatype_dict = {
    cl.channel_type.FLOAT: np.float32,
    cl.channel_type.UNSIGNED_INT8: np.uint8,
    cl.channel_type.UNSIGNED_INT16: np.uint16,
    cl.channel_type.SIGNED_INT8: np.int8,
    cl.channel_type.SIGNED_INT16: np.int16,
    cl.channel_type.SIGNED_INT32: np.int32,
}

cl_image_datatype_dict.update(
    {dtype: cltype for cltype, dtype in list(cl_image_datatype_dict.items())}
)

cl_buffer_datatype_dict = {
    np.bool: "bool",
    np.uint8: "uchar",
    np.uint16: "ushort",
    np.uint32: "uint",
    np.uint64: "ulong",
    np.int8: "char",
    np.int16: "short",
    np.int32: "int",
    np.int64: "long",
    np.float32: "float",
    np.complex64: "cfloat_t",
}


if characterize.has_double_support(get_device().device):
    cl_buffer_datatype_dict[np.float64] = "double"


def abspath(myPath):
    """ Get absolute path to resource, works for dev and for PyInstaller """

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        return os.path.join(base_path, os.path.basename(myPath))
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(base_path, myPath)


def assert_supported_ndarray_type(dtype):
    # make sure it works for e.g. np.float32 and np.dtype(np.float32)
    dtype = getattr(dtype, "type", dtype)
    if dtype not in cl_buffer_datatype_dict:
        raise KeyError("dtype %s not supported " % dtype)


def assert_bufs_type(mytype, *bufs):
    if not all([b.dtype.type == mytype for b in bufs]):
        raise TypeError(
            "all data type of buffer(s) should be %s! but are %s"
            % (mytype, str([b.dtype.type for b in bufs]))
        )

def prepare(arr):
    return np.require(arr, None, "C")

class OCLArray(array.Array, np.lib.mixins.NDArrayOperatorsMixin):


    @classmethod
    def from_array(cls, arr, *args, **kwargs):
        assert_supported_ndarray_type(arr.dtype.type)
        queue = get_device().queue
        return OCLArray.to_device(queue, prepare(arr), *args, **kwargs)

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        assert_supported_ndarray_type(dtype)
        queue = get_device().queue
        return OCLArray(queue, shape, dtype)

    @classmethod
    def empty_like(cls, arr):
        assert_supported_ndarray_type(arr.dtype.type)
        queue = get_device().queue # todo: get queue from arr
        return OCLArray(queue, arr.shape, arr.dtype.type)

    @classmethod
    def zeros(cls, shape, dtype=np.float32):
        assert_supported_ndarray_type(dtype)
        queue = get_device().queue
        new_array = OCLArray(queue, shape, dtype)
        from .._tier1 import set
        set(new_array, 0)
        return new_array

    @classmethod
    def zeros_like(cls, arr):
        assert_supported_ndarray_type(arr.dtype.type)
        queue = get_device().queue
        return cls.zeros(queue, arr.shape, arr.dtype.type)

    def copy_buffer(self, buf, **kwargs):
        queue = get_device().queue
        return cl.enqueue_copy(queue, self.data, buf.data, **kwargs)

    def write_array(self, arr, **kwargs):
        assert_supported_ndarray_type(arr.dtype.type)
        queue = get_device().queue
        return cl.enqueue_copy(queue, self.data, prepare(arr), **kwargs)


    def __array__(self, dtype=None):
        return self.get().astype(dtype)

    @classmethod
    def to_device(cls, queue, ary, *args, **kwargs):
        if isinstance(ary, OCLArray):
            return ary
        cl_a = OCLArray(queue, ary.shape, ary.dtype, strides=ary.strides)
        cl_a.set(ary, queue=queue)
        return cl_a

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method == "__call__":
            func = getattr(OCLArray, f'__{ufunc.__name__}__', None)
            if func is not None:
                return func(*[OCLArray.to_device(self.queue, i) for i in inputs], **kwargs)
        return NotImplemented

    def copy_image(self, img, **kwargs):
        queue = get_device().queue
        return cl.enqueue_copy(
            queue,
            self.data,
            img,
            offset=0,
            origin=(0,) * len(img.shape),
            region=img.shape,
            **kwargs,
        )

    def wrap_module_func(mod, f):
        def func(self, *args, **kwargs):
            return getattr(mod, f)(self, *args, **kwargs)

        return func

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

    # TODO: Not sure if the following are necessary / could be circumvented.
    #       For now tests fail if we remove them.
    def __iadd__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)) :
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(temp, x2, x1)

    def __sub__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(x1, scalar=-x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(x1, x2, factor2=-1)

    def __div__(x1, x2):
        if isinstance(x2, (int, float)):
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
        if isinstance(x2, (int, float)):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
        else:
            from .._tier1 import divide_images
            return divide_images(temp, x2, x1)

    def __itruediv__(x1, x2):
        return x1.__idiv__(x2)

    def __mul__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(x1, x2)

    def __imul__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(temp, x2, x1)

    def __gt__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import greater_constant
            return greater_constant(x1, constant=x2)
        else:
            from .._tier1 import greater
            return greater(x1, x2)

    def __ge__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import greater_or_equal_constant
            return greater_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import greater_or_equal
            return greater_or_equal(x1, x2)

    def __lt__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import smaller_constant
            return smaller_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller
            return smaller(x1, x2)

    def __le__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import smaller_or_equal_constant
            return smaller_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller_or_equal
            return smaller_or_equal(x1, x2)

    def __eq__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import equal_constant
            return equal_constant(x1, constant=x2)
        else:
            from .._tier1 import equal
            return equal(x1, x2)

    def __ne__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import not_equal_constant
            return not_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import not_equal
            return not_equal(x1, x2)

    def __pow__(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import power
            return power(x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(x1, x2)

    def __ipow__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)):
            from .._tier1 import power
            return power(temp, x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(temp, x2, x1)


class _OCLImage:
    def __init__(self, cl_image : cl.Image):
        self.data = cl_image
        self.shape = cl_image.shape[::-1]
        self.dtype = cl_image.dtype
