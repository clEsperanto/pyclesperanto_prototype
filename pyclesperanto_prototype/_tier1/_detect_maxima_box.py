from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def detect_maxima_box(src :Image, dst :Image = None):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    # todo: ensure detect_maxima_2d_x.cl fit to naming convention
    execute(__file__, 'detect_maxima_' + str(len(dst.shape)) + 'd_x.cl', 'detect_maxima_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return dst
