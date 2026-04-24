import numpy as np
from ._pycl import OCLArray, _OCLImage
import pyopencl as cl
from typing import Union

try:
    import pyclesperanto_opencl
    import pyclesperanto_cuda
    Image = Union[np.ndarray, OCLArray, cl.Image, _OCLImage, pyclesperanto_opencl._pyclesperanto._Array, pyclesperanto_cuda._pyclesperanto._Array]
except ImportError:
    try:
        import pyclesperanto_opencl
        Image = Union[np.ndarray, OCLArray, cl.Image, _OCLImage, pyclesperanto_opencl._pyclesperanto._Array]
    except ImportError:
        try:
            import pyclesperanto_cuda
            Image = Union[np.ndarray, OCLArray, cl.Image, _OCLImage, pyclesperanto_cuda._pyclesperanto._Array]
        except ImportError:
            Image = Union[np.ndarray, OCLArray, cl.Image, _OCLImage]


def is_image(object):
    return isinstance(object, np.ndarray) or \
           isinstance(object, tuple) or \
           isinstance(object, list) or \
           isinstance(object, OCLArray) or \
           str(type(object)) in ["<class 'cupy._core.core.ndarray'>",
                                 "<class 'dask.array.core.Array'>",
                                 "<class 'xarray.core.dataarray.DataArray'>",
                                 "<class 'resource_backed_dask_array.ResourceBackedDaskArray'>",
                                 "<class 'torch.Tensor'>",
                                 "<class 'pyclesperanto_opencl._pyclesperanto._Array'>",
                                 "<class 'pyclesperanto_cuda._pyclesperanto._Array'>"]
