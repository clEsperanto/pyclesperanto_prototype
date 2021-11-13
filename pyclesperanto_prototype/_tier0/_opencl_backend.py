import numpy as np

from ._pycl import OCLArray

def opencl_backend():
    return OpenCLBackend()

class OpenCLBackend():
    def __init__(self):
        pass

    def array_type(self):
        return OCLArray

    def asarray(self, image):
        return np.asarray(image)
