import numpy as np
import reikna.cluda as cluda
from reikna.core import Annotation, Parameter, Transformation, Type
from reikna.fft import FFT

from .. import create, get_device, push
from .._tier0._pycl import OCLArray


def _convert_axes_to_absolute(dshape, axes):
    """axes = (-2,-1) does not work in reikna, so we have to convert that"""
    if axes is None:
        return None
    elif isinstance(axes, (tuple, list)):
        return tuple(np.arange(len(dshape))[list(axes)])
    else:
        raise NotImplementedError(f"axes {axes} is of unsupported type {type(axes)}")


def _get_complex_trf(arr):
    """On-gpu transformation that transforms a real array to a complex one."""
    complex_dtype = cluda.dtypes.complex_for(arr.dtype)
    return Transformation(
        [
            Parameter("output", Annotation(Type(complex_dtype, arr.shape), "o")),
            Parameter("input", Annotation(arr, "i")),
        ],
        """
        ${output.store_same}(
            COMPLEX_CTR(${output.ctype})(
                ${input.load_same},
                0));
        """,
    )


_PLANS = {}


def get_fft_plan(arr, axes=None, fast_math=True):
    """returns an reikna plan/FFT for `arr`.

    Will cache the compiled plan and reuse.
    """

    axes = _convert_axes_to_absolute(arr.shape, axes)
    key = (arr.shape, arr.dtype, axes, fast_math)
    if key not in _PLANS:
        if np.iscomplexobj(arr):
            fft = FFT(arr, axes=axes)
        else:
            trf = _get_complex_trf(arr)
            fft = FFT(trf.output, axes=axes)
            fft.parameter.input.connect(trf, trf.output, new_input=trf.input)

        thread = cluda.ocl_api().Thread(get_device().queue)
        _PLANS[key] = fft.compile(thread, fast_math=fast_math)
    return _PLANS[key]


def fftn(
    input_arr,
    output_arr=None,
    axes=None,
    inplace=False,
    fast_math=True,
    inverse=False,
) -> OCLArray:
    _isnumpy = isinstance(input_arr, np.ndarray)
    if isinstance(input_arr, OCLArray):
        if input_arr.dtype != np.complex64:
            raise TypeError("OCLArray input_arr has to be of complex64 type")
    elif _isnumpy:
        if not np.issubdtype(input_arr.dtype, np.floating):
            input_arr = input_arr.astype(np.float32)
    else:
        raise TypeError("input_arr must be either OCLArray or np.ndarray")
    if output_arr is not None and inplace:
        raise ValueError("`output_arr` cannot be provided if `inplace` is True")

    plan = get_fft_plan(input_arr, axes=axes, fast_math=fast_math)

    if isinstance(input_arr, np.ndarray):
        arr_dev = push(input_arr)
        res_dev = create(arr_dev, np.complex64)
    else:
        arr_dev = input_arr
        if inplace:
            res_dev = arr_dev
        else:
            res_dev = (
                create(arr_dev, np.complex64) if output_arr is None else output_arr
            )

    plan(res_dev, arr_dev, inverse=inverse)

    if _isnumpy:
        if inplace:
            input_arr[:] = res_dev.get()
        elif output_arr:
            output_arr[:] = res_dev.get()
    return res_dev


def ifftn(
    input_arr,
    output_arr=None,
    axes=None,
    inplace=False,
    fast_math=True,
):
    return fftn(input_arr, output_arr, axes, inplace, fast_math, True)
