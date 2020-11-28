from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_nonzero_pixels_to_pixelindex(input : Image, output : Image, offset : float = 1):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "src":input,
        "offset":int(offset)
    }

    execute(__file__, 'set_nonzero_pixels_to_pixelindex_x.cl', 'set_nonzero_pixels_to_pixelindex', output.shape, parameters);
    return output
