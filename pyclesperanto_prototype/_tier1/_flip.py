from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def flip(src : Image, dst : Image = None, flip_x : bool = True, flip_y : bool = True, flip_z : bool = True):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst,
        "flipx": int(1 if flip_x else 0),
        "flipy": int(1 if flip_y else 0)
    }

    if (len(dst.shape) == 3):
        parameters.update({"flipz": int(1 if flip_z else 0)});

    execute(__file__, 'flip_' + str(len(dst.shape)) + 'd_x.cl', 'flip_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
