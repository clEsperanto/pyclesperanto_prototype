import numpy as np
from ._pycl import OCLArray, _OCLImage
import pyopencl as cl
from typing import Union

Image = Union[np.ndarray, OCLArray, cl.Image, _OCLImage]

def is_image(object):
    return isinstance(object, np.ndarray) or isinstance(object, OCLArray) or str(type(object)) == "<class 'cupy._core.core.ndarray'>"
