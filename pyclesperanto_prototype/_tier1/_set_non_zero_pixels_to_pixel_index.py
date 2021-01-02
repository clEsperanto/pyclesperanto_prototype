from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_non_zero_pixels_to_pixel_index(input : Image, output : Image, offset : float = 1):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "src":input,
        "offset":int(offset)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/set_nonzero_pixels_to_pixelindex_x.cl', 'set_nonzero_pixels_to_pixelindex', output.shape, parameters);
    return output
