

from ..core import execute


def erode_box_slice_by_slice (src, dst):

    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'erode_box_slice_by_slice_' + str(len(dst.shape)) + 'd_x.cl', 'erode_box_slice_by_slice_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

