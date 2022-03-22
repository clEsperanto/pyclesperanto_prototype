from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_non_zero_pixels_to_pixel_index(source : Image, output : Image = None, offset : float = 1) -> Image:
    """Replaces all 0 value pixels in an image with the index of a pixel.

    Parameters
    ----------
    source: Image
    output: Image, optional
    offset: int, optional

    Returns
    -------

    """


    parameters = {
        "dst":output,
        "src":source,
        "offset":int(offset)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/set_nonzero_pixels_to_pixelindex_x.cl', 'set_nonzero_pixels_to_pixelindex', output.shape, parameters);
    return output
