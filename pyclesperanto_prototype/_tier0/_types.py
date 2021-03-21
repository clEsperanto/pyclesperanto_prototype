import numpy as np
from ._pycl import OCLArray, OCLImage
import pyopencl as cl
from typing import Union

Image = Union[np.ndarray, OCLArray, cl.Image, OCLImage]

def is_image(object):
    return isinstance(object, np.ndarray) or isinstance(object, OCLArray)
