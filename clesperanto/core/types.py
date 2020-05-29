import numpy as np
from gputools import OCLArray
from typing import Union

Image = Union[np.ndarray, OCLArray]

def is_image(object):
    return isinstance(object, np.ndarray) or isinstance(object, OCLArray)
