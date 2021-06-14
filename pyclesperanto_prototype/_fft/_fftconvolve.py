from pyopencl.elementwise import ElementwiseKernel
from .. import get_device
from ._fft import fftn, ifftn
from .._tier0._pycl import OCLArray
import numpy as np


_mult_complex = ElementwiseKernel(
    get_device().context,
    "cfloat_t *a, cfloat_t * b",
    "a[i] = cfloat_mul(a[i], b[i])",
    "mult",
)


def fftconvolve(
    data,
    kernel,
    mode="full",
    axes=None,
    output_arr=None,
    inplace=False,
    kernel_is_fft=False,
):

    if data.shape != kernel.shape:
        raise ValueError("in1 and in2 should have the same shape")

    if isinstance(data, np.ndarray):
        data_g = OCLArray.from_array(data.astype(np.complex64))
    else:
        data_g = data

    if isinstance(kernel, np.ndarray):
        kernel_g = OCLArray.from_array(kernel.astype(np.complex64))
    else:
        kernel_g = kernel

    if inplace:
        output_arr = data_g
    else:
        if output_arr is None:
            output_arr = OCLArray.empty(data_g.shape, data_g.dtype)
        output_arr.copy_buffer(data_g)

    if not kernel_is_fft:
        kern_g = OCLArray.empty(kernel_g.shape, kernel_g.dtype)
        kern_g.copy_buffer(kernel_g)
        fftn(kern_g, inplace=True)
    else:
        kern_g = kernel_g

    fftn(output_arr, inplace=True, axes=axes)
    _mult_complex(output_arr, kern_g)

    ifftn(output_arr, inplace=True, axes=axes)
    return output_arr
