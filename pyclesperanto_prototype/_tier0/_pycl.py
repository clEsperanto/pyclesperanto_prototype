import os
import sys
import numpy as np
import pyopencl as cl
from pyopencl import characterize
from pyopencl import array
from typing import Callable, List, Optional
from functools import lru_cache


# TODO: we should discuss whether this collection is actually the best thing to pass
# around. might be better to work lower level with contexts...
class Device:
    """Just a container for a device, context and queue."""

    def __init__(self, device: cl.Device, context: cl.Context, queue: cl.CommandQueue):
        self.device = device
        self.context = context
        self.queue = queue

    def __repr__(self) -> str:
        refs = self.context.reference_count
        return f"<{self.name} on Platform: {self.device.platform.name} ({refs} refs)>"

    @property
    def name(self) -> str:
        return self.device.name


def score_device(dev: cl.Device) -> float:
    score = 4e12 if dev.type == cl.device_type.GPU else 2e12
    score += dev.get_info(cl.device_info.GLOBAL_MEM_SIZE)
    return score


# container for singleton device
class _current_device:
    _instance: Optional[Device] = None
    score_key: Callable[[cl.Device], float] = score_device


def get_device() -> Device:
    """Get the current device GPU class."""
    return _current_device._instance or select_device()


def select_device(name: str = None, dev_type: str = None, score_key=None) -> Device:
    """Set current GPU device based on optional parameters.

    :param name: First device that contains ``name`` will be returned, defaults to None
    :type name: str, optional
    :param dev_type: {'cpu', 'gpu', or None}, defaults to None
    :type dev_type: str, optional
    :param score_key: scoring function, accepts device and returns int, defaults to None
    :type score_key: callable, optional
    :return: The current GPU instance.
    :rtype: GPU
    """
    device = filter_devices(name, dev_type, score_key)[-1]
    if _current_device._instance and device == _current_device._instance.device:
        return _current_device._instance
    context = cl.Context(devices=[device])
    queue = cl.CommandQueue(context)
    _current_device._instance = Device(device, context, queue)
    return _current_device._instance


def filter_devices(
    name: str = None, dev_type: str = None, score_key=None
) -> List[cl.Device]:
    """Filter devices based on various options

    :param name: First device that contains ``name`` will be returned, defaults to None
    :type name: str, optional
    :param dev_type: {'cpu', 'gpu', or None}, defaults to None
    :type dev_type: str, optional
    :param score_key: scoring function, accepts device and returns int, defaults to None
    :type score_key: callable, optional
    :return: list of devices
    :rtype: List[cl.Device]
    """
    devices = []
    for platform in cl.get_platforms():
        for device in platform.get_devices():
            if name and name.lower() in device.name.lower():
                return [device]
            if dev_type is not None:
                if isinstance(dev_type, str):
                    if dev_type.lower() == "cpu":
                        dev_type = cl.device_type.CPU
                    elif dev_type.lower() == "gpu":
                        dev_type = cl.device_type.GPU
                if device.type != dev_type:
                    continue
            devices.append(device)
    return sorted(devices, key=score_key or _current_device.score_key)


def set_device_scoring_key(func: Callable[[cl.Device], int]) -> None:
    if not callable(func):
        raise TypeError(
            "Scoring key must be a callable that takes a device and returns an int"
        )
    try:
        filter_devices(score_key=func)
    except Exception as e:
        raise ValueError(f"Scoring algorithm invalid: {e}")
    _current_device.score_key = func


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


class OCLProgram(cl.Program):
    """ a wrapper class representing a CPU/GPU Program
    example:
         prog = OCLProgram("mykernels.cl",build_options=["-D FLAG"])
    """
    _wait_for_kernel_finish = None

    def __init__(self, file_name=None, src_str=None, build_options=[], dev=None):
        if file_name is not None:
            with open(file_name, "r") as f:
                src_str = f.read()

        if src_str is None:
            raise ValueError("empty src_str! ")

        if dev is None:
            dev = get_device()

        self._dev = dev
        self._kernel_dict = {}
        super().__init__(self._dev.context, src_str)
        self.build(options=build_options)

    def run_kernel(self, name, global_size, local_size, *args, **kwargs):
        if name not in self._kernel_dict:
            self._kernel_dict[name] = getattr(self, name)

        self._kernel_dict[name](
            self._dev.queue, global_size, local_size, *args, **kwargs
        )
        if OCLProgram._wait_for_kernel_finish:
            self._dev.queue.finish()

    @classmethod
    @lru_cache(maxsize=128)
    def from_source(cls, source):
        return cls(src_str=source)


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


def _wrap_OCLArray(cls):
    """
    WRAPPER
    """

    def prepare(arr):
        return np.require(arr, None, "C")

    @classmethod
    def from_array(cls, arr, *args, **kwargs):
        assert_supported_ndarray_type(arr.dtype.type)
        queue = get_device().queue
        return array.to_device(queue, prepare(arr), *args, **kwargs)

    @classmethod
    def empty(cls, shape, dtype=np.float32):
        assert_supported_ndarray_type(dtype)
        queue = get_device().queue
        return array.empty(queue, shape, dtype)

    @classmethod
    def empty_like(cls, arr):
        assert_supported_ndarray_type(arr.dtype.type)
        return cls.empty(arr.shape, arr.dtype.type)

    @classmethod
    def zeros(cls, shape, dtype=np.float32):
        assert_supported_ndarray_type(dtype)
        queue = get_device().queue
        return array.zeros(queue, shape, dtype)

    @classmethod
    def zeros_like(cls, arr):
        assert_supported_ndarray_type(arr.dtype.type)
        queue = get_device().queue
        return array.zeros(queue, arr.shape, arr.dtype.type)

    def copy_buffer(self, buf, **kwargs):
        queue = get_device().queue
        return cl.enqueue_copy(queue, self.data, buf.data, **kwargs)

    def write_array(self, arr, **kwargs):
        assert_supported_ndarray_type(arr.dtype.type)
        queue = get_device().queue
        return cl.enqueue_copy(queue, self.data, prepare(arr), **kwargs)

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

    cls.from_array = from_array
    cls.empty = empty
    cls.empty_like = empty_like
    cls.zeros = zeros
    cls.zeros_like = zeros_like
    cls.copy_buffer = copy_buffer
    cls.copy_image = copy_image
    cls.write_array = write_array

    cls.__array__ = cls.get

    def add(x1, x2):
        if isinstance(x2, (int, float)) :
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(x1, scalar=x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(x1, x2)
    cls.__add__ = add

    def iadd(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)) :
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(temp, x2, x1)
    cls.__iadd__ = iadd

    def sub(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(x1, scalar=-x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(x1, x2, factor2=-1)
    cls.__sub__ = sub

    def isub(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)) :
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(temp, x1, scalar=-x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(temp, x2, x1, factor2=-1)
    cls.__isub__ = isub

    def mul(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(x1, x2)
    cls.__mul__ = mul

    def imul(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(temp, x2, x1)

    cls.__imul__ = imul

    def div(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(x1, scalar=1.0 / x2)
        else:
            from .._tier1 import divide_images
            return divide_images(x1, x2)
    cls.__div__ = div
    cls.__truediv__ = div

    def idiv(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
        else:
            from .._tier1 import divide_images
            return divide_images(temp, x2, x1)
    cls.__idiv__ = idiv
    cls.__itruediv__ = idiv

    def gt(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import greater_constant
            return greater_constant(x1, constant=x2)
        else:
            from .._tier1 import greater
            return greater(x1, x2)
    cls.__gt__ = gt

    def ge(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import greater_or_equal_constant
            return greater_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import greater_or_equal
            return greater_or_equal(x1, x2)
    cls.__ge__ = ge

    def lt(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import smaller_constant
            return smaller_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller
            return smaller(x1, x2)
    cls.__lt__ = lt

    def le(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import smaller_or_equal_constant
            return smaller_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller_or_equal
            return smaller_or_equal(x1, x2)
    cls.__le__ = le

    def eq(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import equal_constant
            return equal_constant(x1, constant=x2)
        else:
            from .._tier1 import equal
            return equal(x1, x2)
    cls.__eq__ = eq

    def ne(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import not_equal_constant
            return not_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import not_equal
            return not_equal(x1, x2)
    cls.__ne__ = ne

    def pos(x1):
        from .._tier1 import copy
        return copy(x1)
    cls.__pos__ = pos

    def neg(x1):
        from .._tier1 import subtract_image_from_scalar
        return subtract_image_from_scalar(x1, scalar=0)
    cls.__neg__ = neg

    def pow(x1, x2):
        if isinstance(x2, (int, float)):
            from .._tier1 import power
            return power(x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(x1, x2)
    cls.__pow__ = pow

    def ipow(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, (int, float)):
            from .._tier1 import power
            return power(temp, x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(temp, x2, x1)
    cls.__ipow__ = ipow

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
    cls.min = min

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
    cls.max = max

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
    cls.sum = sum

    # todo:
    #  __floordiv__(x1, x2)
    #  __mod__(x1, x2)
    #  __matmul__(x1, x2)
    #  __inv__(x1, x2)
    #  __invert__(x1, x2)
    #  __lshift__(x1, x2)
    #  __rshift__(x1, x2)
    # and, or, xor

    for f in ["dot", "vdot"]:
        setattr(cls, f, wrap_module_func(array, f))

    # for f in dir(cl_math):
    #    if callable(getattr(cl.cl_math, f)):
    #        setattr(cls, f, wrap_module_func(cl.cl_math, f))

    # cls.sum = sum
    cls.__name__ = str("OCLArray")
    return cls


OCLArray = _wrap_OCLArray(array.Array)

class _OCLImage:
    def __init__(self, cl_image : cl.Image):
        self.data = cl_image
        self.shape = cl_image.shape[::-1]
        self.dtype = cl_image.dtype
