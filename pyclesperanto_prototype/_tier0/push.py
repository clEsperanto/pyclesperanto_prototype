import numpy as np
from ._pycl import OCLArray


def push(any_array):
    """Push numpy array on device to an OpenCL array on GPU.

    This method does the same as the converters in CLIJ but is less flexible
    https://github.com/clij/clij-core/tree/master/src/main/java/net/haesleinhuepf/clij/converters/implementations

    :param any_array: input numpy array
    :return: opencl-array
    """

    if isinstance(any_array, OCLArray):
        return any_array

    transposed = any_array.astype(np.float32).T
    return OCLArray.from_array(transposed)


def push_zyx(any_array):
    if isinstance(any_array, OCLArray):
        return any_array

    temp = any_array.astype(np.float32)
    return OCLArray.from_array(temp)
