import os
import sys
import warnings

import numpy as np
import pyopencl as cl
from pyopencl import characterize
from pyopencl import array
from ._device import get_device
from ._array_operators import ArrayOperators, cl_buffer_datatype_dict

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



if characterize.has_double_support(get_device().device):
    cl_buffer_datatype_dict[np.float64] = "double"
else:
    warnings.warn("Data type double is not supported by your GPU. Will use float instead.")

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



class OCLArray(ArrayOperators, array.Array, np.lib.mixins.NDArrayOperatorsMixin):


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
        if dtype is None:
            return self.get()
        else:
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

    def astype(self, dtype, copy=None):
        from ._create import create
        if dtype == float or dtype == np.float64:
            dtype = np.float32
        copied = create(self.shape, dtype=dtype)
        from .._tier1 import copy
        return copy(self, copied)

    def wrap_module_func(mod, f):
        def func(self, *args, **kwargs):
            return getattr(mod, f)(self, *args, **kwargs)

        return func


    def _new_with_changes(
            self,
            data,
            offset,
            shape=None,
            dtype=None,
            strides=None,
            queue=None,
            allocator=None,
    ):
        """
        :arg data: *None* means allocate a new array.
        """
        # If we're allocating new data, then there's not likely to be
        # a data dependency. Otherwise, the two arrays should probably
        # share the same events list.
        return OCLArray(
            self.queue if queue is None else queue,
            self.shape if shape is None else shape,
            self.dtype if dtype is None else dtype,
            allocator=self.allocator if allocator is None else allocator,
            strides=self.strides if strides is None else strides,
            data=data,
            offset=offset,
            events=None if data is None else self.events,
        )

class _OCLImage:
    def __init__(self, cl_image : cl.Image):
        self.data = cl_image
        self.shape = cl_image.shape[::-1]
        self.dtype = cl_image.dtype
