import numpy as np
import reikna.cluda as cluda
from reikna.fft import FFTShift

from .. import create, get_device, push


def fftshift(arr, axes=None, output_arr=None, inplace=False):
    shift = FFTShift(arr, axes=axes)
    thread = cluda.ocl_api().Thread(get_device().queue)
    shiftc = shift.compile(thread)

    arr_dev = push(arr) if isinstance(arr, np.ndarray) else arr
    if inplace:
        res_dev = arr_dev
    else:
        res_dev = create(arr_dev) if output_arr is None else output_arr
    shiftc(res_dev, arr_dev)
    return res_dev
