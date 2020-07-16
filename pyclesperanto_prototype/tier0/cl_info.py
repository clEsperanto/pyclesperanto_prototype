from ._pycl import get_gpu

def cl_info():
    gpu = get_gpu()
    device = get_gpu().device
    return [gpu, device];
