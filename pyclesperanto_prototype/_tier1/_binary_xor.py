from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def binary_xor(src1 : Image, src2 : Image, dst : Image = None):
    """
    documentation placeholder
    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'binary_xor_' + str(len(dst.shape)) + 'd_x.cl', 'binary_xor_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
