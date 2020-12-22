import numpy as np
from ._pycl import OCLArray
import pyopencl as cl
from typing import Union

Image = Union[np.ndarray, OCLArray, cl.Image]

def is_image(object):
    return isinstance(object, np.ndarray) or isinstance(object, OCLArray)
