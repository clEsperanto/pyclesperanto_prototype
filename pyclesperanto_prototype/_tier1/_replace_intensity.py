from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def replace_intensity(src : Image, dst : Image = None, value_to_replace : float = 0, value_replacement : float = 1):
    """Replaces a specific intensity in an image with a given new value.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image input, ByRef Image destination, Number oldValue, Number newValue)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_replaceIntensity


    Returns
    -------

    """


    parameters = {
        "dst": dst,
        "src":src,
        "in":float(value_to_replace),
        "out":float(value_replacement)
    }

    execute(__file__, 'replace_intensity_x.cl', 'replace_intensity', dst.shape, parameters)
    return dst
