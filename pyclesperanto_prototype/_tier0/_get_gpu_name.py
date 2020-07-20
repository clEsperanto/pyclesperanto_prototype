
from ._pycl import get_best_device

def get_gpu_name():
    return get_best_device().name