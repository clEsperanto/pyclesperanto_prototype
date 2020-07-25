import pyopencl as cl
import pytest
import numpy as np

from pyclesperanto_prototype import create_image

DEVICES = [
    device for platform in cl.get_platforms() for device in platform.get_devices()
]


@pytest.fixture(params=DEVICES, ids=lambda x: x.name)
def context(request):
    return cl.Context(devices=[request.param])


dtypes = {
    "int8",
    "int16",
    "int32",
    # 'int64',
    "uint8",
    "uint16",
    "uint32",
    # 'uint64',
    "float16",
    "float32",
    # 'float64',
    # "complex64",
}


@pytest.fixture(params=dtypes)
def dtype(request):
    return np.dtype(request.param)


@pytest.mark.parametrize(
    "shape", [(256, 256), (3, 256, 256), (256, 256, 3), (10, 256, 256)]
)
def test_create_image(context, dtype, shape):
    array = np.random.randint(0, 255, shape).astype(dtype)
    create_image(array, context)
