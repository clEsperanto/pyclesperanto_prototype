from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def paste (src : Image, dst : Image = None, destination_x : int = 0, destination_y : int = 0, destination_z : int = 0):
    """
    documentation placeholder
    """


    parameters = {
        "dst":dst,
        "src":src,
        "destination_x": int(destination_x),
        "destination_y": int(destination_y)
    }


    if (len(dst.shape) == 3):
        parameters.update({"destination_z": int(destination_z)});

    execute(__file__, 'paste_' + str(len(dst.shape)) + 'd_x.cl', 'paste_' + str(len(dst.shape)) + 'd', src.shape, parameters)
    return dst
