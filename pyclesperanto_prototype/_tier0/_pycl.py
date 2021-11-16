import os
import sys
import warnings

import numpy as np
import pyopencl as cl
from pyopencl import characterize
from pyopencl import array
from ._device import get_device
from ._utils import prepare

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
    int: "int",
    float: "float",
    np.float64: "float",
}


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

_supported_numeric_types = (int, float, np.uint16)

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
        if isinstance(x2, _supported_numeric_types) :
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(temp, x2, x1)

    def __sub__(x1, x2):
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

    def __setitem__(self, index, value):
        if isinstance(index, list):
            index = tuple(index)
        if isinstance(index, (tuple, np.ndarray)) and index[0] is not None and isinstance(index[0], (tuple, list, np.ndarray)):
            if len(index) == len(self.shape):
                if len(index[0]) > 0:
                    # switch xy in 2D / xz in 3D, because clesperanto expects an X-Y-Z array;
                    # see also https://github.com/clEsperanto/pyclesperanto_prototype/issues/49
                    index = list(index)
                    index[0], index[-1] = index[-1], index[0]
                    # send coordinates to GPU
                    coordinates = OCLArray.to_device(self.queue, np.asarray(index))
                    num_coordinates = coordinates.shape[-1]
                    if isinstance(value, (int, float)):
                        # make an array containing new values for every pixel
                        number = value
                        from ._create import create
                        value = create((1, 1, num_coordinates))
                        from .._tier1 import set
                        set(value, number)
                    # overwrite pixels
                    from .._tier1 import write_values_to_positions
                    from .._tier2 import combine_vertically
                    values_and_positions = combine_vertically(coordinates, value)
                    write_values_to_positions(values_and_positions, self)
                return
        return super().__setitem__(index, value)

    def __getitem__(self, index):
        result = None
        if isinstance(index, list):
            index = tuple(index)
        if isinstance(index, (tuple, np.ndarray)) and index[0] is not None and isinstance(index[0], (tuple, list, np.ndarray)):
            if len(index) == len(self.shape):
                if len(index[0]) > 0:
                    # switch xy in 2D / xz in 3D, because clesperanto expects an X-Y-Z array;
                    # see also https://github.com/clEsperanto/pyclesperanto_prototype/issues/49
                    index = list(index)
                    index[0], index[-1] = index[-1], index[0]
                    # send coordinates to GPU
                    coordinates = OCLArray.to_device(self.queue, np.asarray(index))
                    # read values from positions
                    from .._tier1 import read_intensities_from_positions
                    result = read_intensities_from_positions(coordinates, self)
                else:
                    return []

        if result is None:
            result = super().__getitem__(index)
        if result.size == 1 and isinstance(result, (OCLArray, cl.array.Array)):
            result = result.get()
        return result

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
