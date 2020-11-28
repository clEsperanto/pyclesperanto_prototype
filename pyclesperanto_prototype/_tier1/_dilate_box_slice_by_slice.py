from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def dilate_box_slice_by_slice(src : Image, dst : Image = None):

    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'dilate_box_slice_by_slice_' + str(len(dst.shape)) + 'd_x.cl', 'dilate_box_slice_by_slice_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
