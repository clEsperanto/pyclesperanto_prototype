from pyopencl.elementwise import ElementwiseKernel
from .. import get_device
from ._fft import fftn, ifftn
from .._tier0._pycl import OCLArray
import numpy as np
from .. import push, crop

_mult_complex = ElementwiseKernel(
    get_device().context,
    "cfloat_t *a, cfloat_t * b",
    "a[i] = cfloat_mul(a[i], b[i])",
    "mult",
)


def _fix_shape(arr, shape):
    if arr.shape == shape:
        return arr
    if isinstance(arr, OCLArray):
        # TODO
        #raise NotImplementedError("Cannot not resize/convert array to complex type..")
        from .._tier0 import create
        from .._tier1 import set, paste

        result = create(shape, arr.dtype)
        set(result, 0)
        paste(arr, result)
    if isinstance(arr, np.ndarray):
        result = np.zeros(shape, dtype=arr.dtype)
        result[tuple(slice(i) for i in arr.shape)] = arr
    return result


def fftconvolve(
    data,
    kernel,
    mode="same",
    axes=None,
    output_arr=None,
    inplace=False,
    kernel_is_fft=False,
):
    if mode not in {"valid", "same", "full"}:
        raise ValueError("acceptable mode flags are 'valid', 'same', or 'full'")
    if data.ndim != kernel.ndim:
        raise ValueError("data and kernel should have the same dimensionality")

    # expand arrays
    s1 = data.shape
    s2 = kernel.shape
    axes = tuple(range(len(s1))) if axes is None else tuple(axes)
    shape = [
        max((s1[i], s2[i])) if i not in axes else s1[i] + s2[i] - 1
        for i in range(data.ndim)
    ]
    data = _fix_shape(data, shape)
    kernel = _fix_shape(kernel, shape)

    if data.shape != kernel.shape:
        raise ValueError("in1 and in2 must have the same shape")

    data_g = push(data, np.complex64)
    kernel_g = push(kernel, np.complex64)

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

    _out = output_arr.real if np.isrealobj(data) else output_arr

    if mode == "full":
        return _out
    elif mode == "same":
        return _crop_centered(_out, s1)
    else:
        shape_valid = [
            _out.shape[a] if a not in axes else s1[a] - s2[a] + 1
            for a in range(_out.ndim)
        ]
        return _crop_centered(_out, shape_valid)
    return _out


def _crop_centered(arr, newshape):
    # Return the center newshape portion of the array.
    newshape = np.asarray(newshape)
    currshape = np.array(arr.shape)
    startind = (currshape - newshape) // 2
    return crop(
        arr,
        start_y=startind[0],
        start_x=startind[1],
        height=newshape[0],
        width=newshape[1],
    )
